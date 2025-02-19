import json
import pathlib
from logging import Logger as L
from logging.config import dictConfig


class LoggerMeta(type):
    """
    In python, a metaclass is a "class of classes", meaning it defines how classes are created and behave.
    📌 EXTRA:
        - When you define a class in Python, it is actually an instance of a metaclass.
        - By default, all classes in Python use type as the metaclass.
    """

    def __getattr__(cls, name):
        """
        Gets called when the item is not found via __getattribute__
        In this case, it is used to get the logger instance and call the method on it.
        """
        return getattr(cls.logger(), name)


class Logger(metaclass=LoggerMeta):
    _logger: L
    executed: bool = False

    @classmethod
    def logger(cls) -> L:
        if cls.executed:
            return cls._logger

        config = json.loads(pathlib.Path("config/config_log.json").read_bytes())
        dictConfig(config)
        cls.executed = True

        return cls._logger
