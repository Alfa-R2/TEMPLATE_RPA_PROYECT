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

import json
import pathlib
from logging import Logger as L
from logging import getLogger
from logging.config import dictConfig

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

    _logger: L = getLogger("json_logger")
    executed: bool = False

    @classmethod
    def logger(cls) -> L:
        if cls.executed:
            return cls._logger

        config: dict = json.loads(pathlib.Path("config/config_log.json").read_bytes())
        config["formatters"].update(formatter)
        config["handlers"].update(handler)
        config["loggers"].update(logger)
        dictConfig(config)
        cls.executed = True

        return cls._logger


formatter = {
    "json": {
        "()": "src.logger.formats.jsonlogger.JsonFormatter",
        "fmt_keys": {
            "level": "levelname",
            "message": "message",
            "timestamp": "timestamp",
            "logger": "name",
            "module": "module",
            "function": "funcName",
            "line": "lineno",
            "thread_name": "threadName",
        },
    }
}

handler = {
    "json_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "level": "DEBUG",
        "formatter": "json",
        "filename": "app.log.jsonl",
        "maxBytes": 1000000,
        "backupCount": 3,
    }
}

logger = {
    "json_logger": {
        "level": "DEBUG",
        "handlers": ["stderr", "json_file"],
        "propagate": "false",
    },
}
