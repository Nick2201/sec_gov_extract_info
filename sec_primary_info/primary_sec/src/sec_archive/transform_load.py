import zipfile
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import re

import time
import logging

import sys, os

sys.path.insert(0, os.getcwd())

from primary_sec.utils.data_bases import report_liks, engine, conn

logging.basicConfig(
    filename=r'sec_archive_links.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

"""
    Walk throw all files in Zip Folder
"""
# with zipfile.ZipFile(zip_archive, "r") as archive:
#     for filename in zip_ref.namelist():
#         file_data = zip_ref.read(filename)

"""
    Read One Ticker Json
"""
# with open(tickers_json, "r") as read_file:
#     data = json.load(read_file)
"""

"""

current_path = Path(Path.cwd() / "primary_sec").absolute()
DOCS_FOLDER = Path(current_path / "docs")
SETTINGS_FOLDER = Path(current_path / 'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER / "db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)

zip_archive_path = Path(DOCS_FOLDER / 'companyfacts.zip').absolute()
error_file = Path(DOCS_FOLDER / "error.txt")
# with zipfile.ZipFile(zip_archive_path, "r") as archive:
#     for filename in zip_ref.namelist():
#         zip_archive = zip_ref.read(filename)

SEC_URL_BASE = 'https://www.sec.gov/Archives/edgar/data/'
'''
    PatternRefactor:
        - Chain of responsability
        - Strategy
'''


def convert_periods_to_quartals(fp: str) -> str:
    return 4 if fp == "FY" else int(fp[1:])


def create_urls(accn_value: str, cik: str) -> str:
    return SEC_URL_BASE + cik + '/' + re.sub("-", "", accn_value)


def mapping_cik(cik_row: str) -> str:
    return str(cik_row).zfill(10)


def transform(data: Dict) -> List:
    """
        Troubles:
            -
        'cik',
        "date_publication"  : report publication date,
        'quartal'           : number of quartal [1-4],
        'date_added'        : date when push in DB,
        'url_report'

    """

    date_added = datetime.date(datetime.now())
    cik = mapping_cik(data['cik'])
    entity = data['entityName']
    cik_rows = []
    for i in data['facts']["us-gaap"]["Assets"]['units']["USD"]:
        table_dict = {}
        table_dict['cik'] = cik
        table_dict['date_publication'] = i["filed"]
        table_dict['quartal'] = convert_periods_to_quartals(i["fp"])
        table_dict['date_added'] = date_added
        table_dict['url_report'] = create_urls(accn_value=i['accn'], cik=cik),
        cik_rows.append(table_dict)

    return cik_rows


def company_facts_load(_data):
    '''FROM One dict FROM one json doc,like <<'CIK0000894315'.json>>
    transform speccific values and push into db
    '''
    extracted_data = transform(_data)
    for _row in extracted_data:
        try:
            ins = report_liks.insert().values(**_row)

            logging.info(str({_row['cik']: [
                _row['date_publication'],
                _row['date_added']
            ]}) + "data inserted into database")
            conn.execute(ins)
            print(f"{_row['cik']} is")
            conn.commit()
        except:
            conn.rollback()
            logging.warning(str({_row['cik']: [
                _row['date_publication'],
                _row['date_added']
            ]}) + "data could not be inserted into database")
    # conn.close()


def archive_load(zip_archive_path=zip_archive_path):  # Path
    succses_count = 0
    error_count = 0

    with zipfile.ZipFile(zip_archive_path, "r") as archive:
        for filename in archive.namelist():
            start_time = time.time()
            file_data = archive.read(filename)
            try:
                with archive.open(filename) as read_file:
                    json_data = json.load(read_file)
                    company_facts_load(json_data)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"{filename}: DOWNLOAD :: Elapsed time: {elapsed_time:.2f} seconds")
                    succses_count += 1
            except Exception as err:
                with open(error_file, 'a') as read_file:
                    read_file.write(f'{filename}:{err}\n')
                    print(f"IN {filename} have error as {err}")
                    error_count += 1
                continue
            finally:
                print(f"succses_count: {succses_count} --- error_count: {error_count}")


if __name__ == '__main__':
    docs = [
        'CIK0000894315',  # 1
        'CIK0000019617',  # 2
        'CIK0000946647',  # 3
        'CIK0000039263',  # 4
    ]

    json_name = Path(DOCS_FOLDER / f'{docs[3]}.json')
    # Получение текущего пути
    print(zip_archive_path)

    # archive_load()
    # Путь к корневой папке проекта

    # with zipfile.ZipFile(zip_archive_path, "r") as archive:
    #     for filename in zip_ref.namelist():
    #         zip_archive = zip_ref.read(filename)
    # print(zip_archive_path)
    # archive_load(zip_archive)
    # print(current_path)
    # with open(json_name, "r") as read_file:
    #     data = json.load(read_file)
    #     company_facts_load(data)
