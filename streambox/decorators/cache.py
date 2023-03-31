import datetime
import logging
import pickle
import json
import os


NO_CACHE = object()  # A unique object used to represent "do not cache" flag


def cache(expiry=datetime.timedelta(minutes=30), persistent=False, ttl=0, no_cache=None, show_log=False, timer=False):
    """
    A caching decorator that caches the results of a function for a specified
    amount of time and optionally saves the cache data to disk using pickle.

    :param expiry: A datetime.timedelta object specifying the cache expiry time.
    :param persistent: A boolean flag indicating whether to save the cache data to disk using pickle.
    :param ttl: A float specifying the maximum allowed execution time for the decorated function.
    :param no_cache: A unique object used to indicate that the decorated function should not be cached.
    :param show_log: A boolean flag indicating whether to log a message when the caching mechanism is triggered.
    :param timer: A boolean flag indicating whether to log execution time message when the caching mechanism is triggered.
    """

    def decorator(func):
        cached_results = {}
        pickle_file = f'../data/{func.__name__}_cache.pickle'

        if persistent and os.path.exists(pickle_file):
            with open(pickle_file, 'rb') as f:
                cached_results = pickle.load(f)

        def wrapper(*args, **kwargs):
            filtered_kwargs = {k: v for k, v in kwargs.items() if not k.startswith('_')}
            key = json.dumps((func.__name__, args, frozenset(filtered_kwargs.items())), sort_keys=True)
            if key in cached_results and datetime.datetime.now() < cached_results[key]['expiry'] and cached_results[key]['ttl'] <= ttl:
                if show_log:
                    logging.info(f"Cache hit for function {func.__name__}")

                if ttl > 0:
                    cached_results[key]['ttl'] += 1

                return cached_results[key]['value']
            else:
                if key in cached_results:
                    del cached_results[key]

                start_time = datetime.datetime.now()
                values = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                execution_time = (end_time - start_time).total_seconds()
                if no_cache is not None and no_cache in values:
                    return values
                else:
                    if isinstance(values, tuple):
                        cached_results[key] = {'value': tuple(values),
                                               'expiry': datetime.datetime.now() + expiry,
                                               'ttl': 0}
                    else:
                        cached_results[key] = {'value': values,
                                               'expiry': datetime.datetime.now() + expiry,
                                               'ttl': 0}
                    if persistent:
                        with open(pickle_file, 'wb') as f:
                            pickle.dump(cached_results, f)
                    if show_log:
                        logging.info(f"Caching results for function {func.__name__}")
                    if timer:
                        logging.info(f'Execution time: {execution_time} seconds')
                    return cached_results[key]['value']

        return wrapper

    return decorator
