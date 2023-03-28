import logging
import functools
import inspect
from timeutils import Stopwatch

logger_default = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def timer(msg_template=None,
          level=logging.INFO,
          prefix=None,
          suffix=None,
          logger=logger_default):
    def decorator(func):
        sig = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args, **kw):
            if logger.isEnabledFor(level):
                if msg_template:
                    bound_args = sig.bind(*args, **kw)
                    bound_args.apply_defaults()
                    msg = msg_template.format_map(bound_args.arguments)
                else:
                    msg = f'{func.__name__}'

                if prefix:
                    bound_args = sig.bind(*args, **kw)
                    bound_args.apply_defaults()
                    msg = prefix.format_map(bound_args.arguments) + msg

                if suffix:
                    bound_args = sig.bind(*args, **kw)
                    bound_args.apply_defaults()
                    msg = msg + suffix.format_map(bound_args.arguments)

                # logger.log(level, msg)

            sw = Stopwatch(start=True)
            result = func(*args, **kw)

            if logger.isEnabledFor(level):
                logger.log(level, f'{msg} in {sw.elapsed}')
            return result

        return wrapper

    return decorator
