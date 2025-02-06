import json
import pathlib
from logging import Logger as L
from logging.config import dictConfig


class LoggerMeta(type):
    def __getattr__(cls, name):
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
