import sys

from .log_filters import DebugInfoLogFilter, ErrorLogFilter


logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "#%(levelname)-8s %(name)s:%(funcName)s - %(message)s"
        },
        "formatter_1": {
            "format": "[%(asctime)s] #%(levelname)-8s %(filename)s:"
                      "%(lineno)d - %(name)s:%(funcName)s - %(message)s"
        }
    },
    "filters": {
        "error_filter": {
            "()": ErrorLogFilter,
        },
        "debug_info_filter": {
            "()": DebugInfoLogFilter,
        }
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "default"
        },
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "filters": ["debug_info_filter", ],
            "stream": sys.stdout
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": "error.log",
            "mode": "w",
            "level": "DEBUG",
            "formatter": "formatter_1",
            "filters": ["error_filter"]
        },
    },
    "loggers": {
        "__main__": {
            "level": "INFO",
            "formatter": "default",
            "handlers": ["default"]
        },
        "handlers.user_handlers": {
            "level": "INFO",
            "handlers": ["stdout", "error_file"]
        },
        "handlers.other_handlers": {
            "level": "INFO",
            "handlers": ["stdout"]
        },
    },
}