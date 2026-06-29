import logging
from pathlib import Path


class LoggingService:

    def __init__(self):

        log_dir = (
            Path.home()
            / ".narratorpro"
            / "logs"
        )

        log_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            handlers=[
                logging.FileHandler(
                    log_dir / "narratorpro.log",
                    encoding="utf-8",
                ),
                logging.StreamHandler(),
            ],
        )

        self.logger = logging.getLogger("NarratorPro")

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)