import sys,os

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from pathlib import Path
from bs4 import BeautifulSoup
import json
current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)



def driver_func():

    option = webdriver.FirefoxOptions()
    option.set_preference('dom.webdriver.enabled', True)

    option.set_preference('dom.webnotifications.enebled', False)
    option.set_preference('media.volume_scale', '0.0')

    option.set_preference("browser.download.folderList", 2)
    option.set_preference("browser.download.manager.showWhenStarting", False)

    option.set_preference("browser.download.dir", str(DOCS_FOLDER))
#     option.set_preference("browser.helperApps.neverAsk.saveToDisk","text/xlsx")
    option.set_preference('browser.helperApps.neverAsk.saveToDisk',
                          'text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    option.headless = True  # True - скрывает отображение работы браузера

    return webdriver.Firefox(executable_path=r"\geckodriver.exe", options=option)


