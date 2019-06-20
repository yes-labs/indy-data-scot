import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(name)s:%(levelname)s::%(message)s")
logger = logging.getLogger(__name__)


class NoDataFoundError(RuntimeError):
    def __init__(self, msg=""):
        self.msg = msg
        logger.error(self.msg)

    def __str__(self):
        return self.msg


class DataFormatDoesntMatchExpectedError(ValueError):
    def __init__(self, msg=""):
        self.msg = msg
        logger.error(self.msg)

    def __str__(self):
        return self.msg
