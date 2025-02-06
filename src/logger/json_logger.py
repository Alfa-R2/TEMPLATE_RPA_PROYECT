"""
    Example:
        JSONLogger.debug("debug message", extra={"x": "hello"})
        JSONLogger.info("info message")
        JSONLogger.warning("warning message")
        JSONLogger.error("error message")
        JSONLogger.critical("critical message")

        try:
            1 / 0
        except ZeroDivisionError:
            JSONLogger.exception("exception message")
"""

import logging.config
import logging.handlers
from logging import Logger as L

from .core.logger import Logger


class JSONLogger(Logger):
    """
    :method   debug("debug message", extra={"x": "hello"})
    :method   info("info message")
    :method   warning("warning message")
    :method   error("error message")
    :method   critical("critical message")
    :method   exception("exception message")
    """

    _logger: L = logging.getLogger("json_logger")
    executed: bool = False
