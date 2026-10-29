import logging
import logging.config
import os

from musix_app.core import app_config
from musix_app.core.system_info import get_system_info

LOG_FOLDER_NAME = "LOGS"
LOG_FILE_NAME = "musix.log"

_CONSOLE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_FILE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(module)s:%(lineno)d | %(message)s"


def get_log_dir() -> str:
    user_home = get_system_info().USER_HOME
    return os.path.join(user_home, app_config.application["HOME_FOLDER"], LOG_FOLDER_NAME)


def setup_logging() -> None:
    level = os.environ.get("LOG_LEVEL", "INFO").upper()
    log_dir = get_log_dir()
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, LOG_FILE_NAME)

    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": _CONSOLE_FORMAT,
                "datefmt": "%H:%M:%S",
            },
            "file": {
                "format": _FILE_FORMAT,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": level,
                "formatter": "console",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": level,
                "formatter": "file",
                "filename": log_file,
                "maxBytes": 5 * 1024 * 1024,
                "backupCount": 5,
                "encoding": "utf-8",
            },
        },
        "loggers": {
            "musix": {"level": level, "handlers": ["console", "file"], "propagate": False},
            "uvicorn": {"level": level, "handlers": ["console", "file"], "propagate": False},
            "uvicorn.error": {"level": level, "handlers": ["console", "file"], "propagate": False},
            "uvicorn.access": {"level": level, "handlers": ["console", "file"], "propagate": False},
        },
        "root": {"level": level, "handlers": ["console", "file"]},
    })


def get_logger(name: str = "musix") -> logging.Logger:
    return logging.getLogger(name)
