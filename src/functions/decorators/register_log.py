import functools
from typing import Callable, Type

from src.logger.core.logger import Logger


def register_exception_logger(logger: Type[Logger]):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.exception(e)
                return None

        return wrapper

    return decorator
