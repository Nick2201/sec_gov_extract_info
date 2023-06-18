import zipfile
from transform_load import (
    load_archive,
    load_to_db)

from extract import download_zip_file

import logging

from pathlib import Path
import json
current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)

# SRC = Path(current_path/"src")
# SEC_PRIM = Path(SRC/"sec_archive")
# SRC_DOCS = Path(SEC_PRIM/"docs")
# # zip_archive_path = Path(SRC_DOCS/'companyfacts.zip')
# SRC = Path(current_path/"src")
# SEC_PRIM = Path(SRC/"sec_archive")
# SRC_DOCS = Path(SEC_PRIM/"docs")
zip_archive_path = Path(DOCS_FOLDER/'companyfacts.zip')



error_file = Path(DOCS_FOLDER/"error.txt")

''' TODO: extracter_archive
    extracter_archive.extract()
    extracter_archive.transform()
    extracter_archive.load()
'''
class DownloadModule:
    def __init__(self,main_link):
        self.main_link= main_link


        self.extracted_data = None
        self.transformed_data = None
        self.loaded_data = None


    def extract(self):
        download_zip_file()

        logging.info(f'{strftime("%Y-%m-%d %H:%M:%S", gmtime())} last time updated')
        print("ARCHIVE DOWNLOADED")

    def transform(self):
        transform()

    def load(self,_data:dict):
        load_to_db(_data)
        print(f"DATA {_data} have pushed to DB")

    def load_big(self):
        print(zip_archive_path.absolute())
        load_archive(zip_archive_path=str(zip_archive_path.absolute()))
        print("archive_pushed")

extracter_archive = DownloadModule(
    main_link="http://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip",
    )
'''
    PUSH TRANSFORMED + LOAD into postgres db
'''

# with zipfile.ZipFile(zip_archive_path, "r") as archive:
#     for filename in zip_ref.namelist():
#         zip_archive = zip_ref.read(filename)
def push_sec_arch_db():
    extracter_archive.load_big()

def download_archive():
    extracter_archive.extract()
download_archive()
push_sec_arch_db()