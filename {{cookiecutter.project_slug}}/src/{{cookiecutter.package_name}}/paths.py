from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Paths:
    """
    Class to store paths such as bot's root, config, src directories, etc.
    """

    ROOT: Path
    DOT_DATA: Path
    CONFIG_DIR: Path
    PROJECT_DIR: Path
    LOGS_DIR: Path

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
        parents = Path(bot_path).parents
        root = parents[2]
        config_dir = root / "config"
        project_dir = parents[0]
        dot_data = root / ".data"
        logs_dir = dot_data / "logs"

        for path in [logs_dir]:
            path.mkdir(parents=True, exist_ok=True)

        return cls(
            ROOT=root,
            PROJECT_DIR=project_dir,
            CONFIG_DIR=config_dir,
            DOT_DATA=dot_data,
            LOGS_DIR=logs_dir,
        )
