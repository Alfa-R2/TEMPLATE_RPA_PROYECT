from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Paths:
    """
    Class to store paths such as bot's root, config, src directories, etc.
    """

    ROOT: Path
    CONFIG_DIR: Path
    SRC_DIR: Path

    @classmethod
    def from_config(cls, bot_path: str, cp: ConfigParser | None = None) -> "Paths":
        """
        Create Paths object from bot's root path and ConfigParser object.

        Parameters:
            bot_path (str): It's the path where __init__.py is called.
            cp (ConfigParser): A ConfigParser object to read the configuration file

        Returns:
            Paths: A instance of Paths.
        """
        root = Path(bot_path).parents[1]
        config_dir = root / "config"
        src_dir = root / "src"
        return cls(
            ROOT=root,
            CONFIG_DIR=config_dir,
            SRC_DIR=src_dir,
        )
