import functools
import time
from logging import error
from typing import Callable


def retry(max_retries: int, delay: int, exceptions: tuple = (Exception,)) -> Callable:
    def decorator_retry(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs) -> Callable:
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Error: {e}, retrying in {delay} seconds, itento : {i+1}")
                    time.sleep(delay)
            error(last_exception, exc_info=True)
            raise last_exception

        return wrapper_retry

    return decorator_retry
