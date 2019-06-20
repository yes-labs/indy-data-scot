import logging
import os

import urllib3

# import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s")
logger = logging.getLogger(__name__)


class NoDataFound(RuntimeError):
    def __init__(self, msg=""):
        self.msg = msg
        logger.error(self.msg)

    def __str__(self):
        return self.msg


def download_file(source_url: str) -> str:
    """
    if the file hasn't been downloaded, then let's download it
    for now this just downloads to current working directory
    it would be better to have a dedicated path for raw data and processed data

    :return: destination_path
    """
    destination_path = os.path.join(os.getcwd(), "income_tax_gender_region_country.xlsx")
    if not os.path.isfile(destination_path):
        logger.info(f"downloading from {source_url} into {destination_path}")
        http = urllib3.PoolManager()
        r = http.request("GET", source_url, preload_content=False)
        with open(destination_path, "wb") as out:
            while True:
                chunk_size = 65536  # 64 kb
                data = r.read(chunk_size)
                if not data:
                    raise NoDataFound("couldn't find any data at source url")
                out.write(data)
        r.release_conn()
        logger.info("download complete")
    else:
        logger.info(f"not downloading file because {destination_path} already exists")
    return destination_path


# def extract_df(valid_row) -> pd.DataFrame:
#     """
#     given a sheet with a bunch of stuff on it
#     """
