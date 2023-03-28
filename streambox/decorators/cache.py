import json


def cache(func):
    cache_data = {}

    def wrapper(*args, **kwargs):
        checked_kwargs = kwargs.copy()
        for key in checked_kwargs.keys():
            if key[0] == '_':
                # those arguments starting with _ will be removed
                del kwargs[key]

        arguments = {"args": args, "kwargs": kwargs}
        json_arg = json.dumps(arguments)
        if json_arg in cache_data:
            return cache_data[json_arg]
        else:
            result = func(*args, **kwargs)
            cache_data[json_arg] = result
            return result

    return wrapper
