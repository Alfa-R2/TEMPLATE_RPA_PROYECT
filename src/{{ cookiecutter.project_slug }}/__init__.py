"""
Optional:
    from configparser import ConfigParser
    cp = ConfigParser()
    cp.read("config.ini")

"""

from .logger import set_logger
from .paths import Paths

paths = Paths.from_config(__file__)

set_logger(paths.LOGS_DIR)
