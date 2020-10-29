from .command import *

import logging
from colorlog import ColoredFormatter

logger = logging.getLogger("jarvis.ext.commands")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(
    ColoredFormatter(
        "{log_color}{levelname:-8}{reset} {white}{message}",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style='{'
    )
)
logger.addHandler(streamHandler)
