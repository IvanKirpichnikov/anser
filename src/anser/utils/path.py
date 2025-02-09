import os
from pathlib import Path

from anser.entities.file_names import ANSER_CONFIG


def get_absolute_path(path: str | None = None) -> Path:
    return Path(os.path.abspath(path or os.getcwd()))


def build_config_path(path: str | None = None) -> Path:
    if path:
        return Path(path)
    return get_absolute_path() / ANSER_CONFIG
