from .transform import (
load_to_db)
from .extract import DownloadModule

import logging

from pathlib import Path
import json

current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)

tickers_json = Path(DOCS_FOLDER/'tickers.json')

extract_tickers = DownloadModule(
    main_link="https://www.sec.gov/files/company_tickers.json"
)
extract_tickers.extract()
extract_tickers.transform()
extract_tickers.load_to_json_file(tickers_json)

'''
    PUSH TRANSFORMED + LOAD into postgres db
'''
# load_to_db(tickers_json)

def tickers_extract():
    extract_tickers.extract()