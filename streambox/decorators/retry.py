import time
from functools import wraps
import logging

logger_default = logging.getLogger(__name__)


def retry(max_tries=5, delay_seconds=None, incremental_delay=10):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            for attempt in range(1, max_tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if delay_seconds is None:
                        delayed_run = incremental_delay * attempt
                    else:
                        delayed_run = delay_seconds

                    logger_default.exception("Try number %s/%s has failed (will wait %ss until next try) : %s",
                                             attempt,
                                             max_tries,
                                             str(delayed_run),
                                             (args, kwargs))
                    time.sleep(delayed_run)
            logger_default.critical("All %s tries have failed : %s",
                                    max_tries,
                                    (args, kwargs))
        return wrapper_function

    return decorator_retry
