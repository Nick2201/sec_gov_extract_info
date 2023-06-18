
from primary_sec.utils.driver_gecko import driver_func


import logging
from pathlib import Path

import json
current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)


logging.basicConfig(
    filemode=r'/primary_sec/logs/primary_info_load.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def download_zip_file(url_archive: str = "http://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip"):
    # create a webdriver instance
    driver = driver_func()

    # navigate to the download link
    driver.get(url_archive)

    driver.quit()
def main():
    print(SETTING_FOLDER)