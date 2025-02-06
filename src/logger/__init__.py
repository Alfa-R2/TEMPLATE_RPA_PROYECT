"""
    The module logger is a package that contains the next logger classes:
    - FileLogger
    - JSONLogger
"""

from .file_logger import FileLogger
from .json_logger import JSONLogger

__all__ = ["FileLogger", "JSONLogger"]
