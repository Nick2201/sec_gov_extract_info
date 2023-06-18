from time import sleep
from pathlib import Path
from bs4 import BeautifulSoup
import json
from primary_sec.utils.driver_gecko import driver_func
from time import gmtime, strftime
import logging
import sys
# from settings.config import DOCS_FOLDER

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)



class DownloadModule:
    def __init__(self,main_link):
        self.main_link= main_link


        self.extracted_data = None
        self.transformed_data = None
        self.loaded_data = None


    def extract(self):
        _driver = driver_func()
        _driver.get(self.main_link)

        logging.info(f'{strftime("%Y-%m-%d %H:%M:%S", gmtime())} last time updated')
        self.extracted_data = _driver.page_source
        print("Load New version \"tickers.json\"")
    def transform(self):

        soup = BeautifulSoup(self.extracted_data, 'lxml')
        json_type = json.loads(soup.find("body").text)
        self.transformed_data = json_type
    def load_to_json_file(self,file_path):

        with open(file_path, 'w',encoding='utf-8') as f:
            json.dump(self.transformed_data, f)
module = DownloadModule(
    main_link="https://www.sec.gov/files/company_tickers.json"
)
def tickers_extract():


    module.extract()

