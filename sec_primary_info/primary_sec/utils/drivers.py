from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from pathlib import Path
from bs4 import BeautifulSoup

class DriverClass:
    def __init__(self):

        self.service_chorme_driver_manager = ChromeDriverManager().install() #
        self.driver_options = webdriver.ChromeOptions()
        # self.driver_options.add_argument("--disable-extensions")
        # self.driver_options.add_argument("--disable-gpu")
        # self.driver_options.add_argument("--headless")

        self._driver = None
    def make_driver(self):
        self._driver = webdriver.Chrome(service=ChromeService(self.service_chorme_driver_manager),options=self.driver_options)
        return self


class FileTemp:
    def __init__(self,file_name,file_extension,main_path):
        self.file_name = file_name
        self.file_extension = file_extension

        self.main_path = main_path
        self.file_path = self.main_path.joinpath((
            self.file_name +
            self.file_extension))
class FilesSystem:
    def __init__(self):
        self.dict_structure = {}

    def _add (self,file_name_api:str,file_:FileTemp):
        self.dict_structure[file_name_api]= file_

# from settings.config import DOCS_FOLDER
_path = r"C:\Users\nickl\My_softwares\bit_bucket_repos\sec_primary_info-1\docs"
main_link="http://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip",

link = "https://www.sec.gov/edgar/sec-api-documentation"
