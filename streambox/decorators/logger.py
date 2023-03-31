import logging
import time

logging.basicConfig(level=logging.INFO)


def logger(timer=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(f'Started executing {func.__name__}')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logging.info(f'Finished executing {func.__name__}')
            if timer:
                logging.info(f'Execution time: {end_time - start_time} seconds')
            return result
        return wrapper
    return decorator
