import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def get_logger():
    Path("logs").mkdir(exist_ok=True)
    logger=logging.getLogger("NarratorPro")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    h=RotatingFileHandler("logs/NarratorPro.log",maxBytes=1_000_000,backupCount=5)
    h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(h)
    return logger
