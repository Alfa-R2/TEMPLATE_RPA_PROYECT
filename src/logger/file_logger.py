"""
    Example:
        FileLogger.debug("debug message")
        FileLogger.info("info message")
        FileLogger.warning("warning message")
        FileLogger.error("error message")
        FileLogger.critical("critical message")

        try:
            1 / 0
        except ZeroDivisionError:
            FileLogger.exception("exception message")
"""

import logging.config
import logging.handlers
from logging import Logger as L

from .core.logger import Logger


class FileLogger(Logger):
    """
    :method   debug("debug message")
    :method   info("info message")
    :method   warning("warning message")
    :method   error("error message")
    :method   critical("critical message")
    :method   exception("exception message")
    """

    _logger: L = logging.getLogger("file_logger")
    executed: bool = False
