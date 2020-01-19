import logging
import sys

VERSION = "0.3.4"
logger = logging.getLogger("cereja")
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
consoleHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(consoleHandler)
logger.setLevel(logging.ERROR)

__all__ = ['VERSION', 'logger', 'set_log_level']

logger.log(50, f"Cereja version: {VERSION}")


def set_log_level(level: int):
    """
    Default log level is INFO

    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    """
    if not isinstance(level, int):
        raise TypeError(f"Value is'nt valid. {set_log_level.__doc__}")
    logger.setLevel(level)
    logger.info(f"Update log level to {level}")
