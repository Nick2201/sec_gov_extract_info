
import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import re


from primary_sec.utils.data_bases import TicketsTable,engine,conn
import logging
import sys,os
sys.path.insert(0, os.getcwd())


logging.basicConfig(
    filename='tickers_load.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)
_tickers_json = Path(DOCS_FOLDER/'tickers.json')
print(_tickers_json)


def mapping_cik(cik_row) ->str:
    return str(cik_row).zfill(10)
"""
    1. 'cik_str': 'cik'
    2. 'ticker' : 'tiker'
    3. 'title'  : 'title'

"""
def transform(data:Dict) -> List:
    date_added = datetime.date(datetime.now())

    cik_rows = []
    for main_index, _value_main in data.items():
        table_dict = {}
        table_dict['cik'] = (mapping_cik(_value_main["cik_str"]))
        table_dict['ticker'] = _value_main['ticker']
        table_dict['title'] = _value_main['title']
        table_dict['date_added'] = date_added
        cik_rows.append(table_dict)

    return cik_rows


def load_to_db(tickers_json:Path=_tickers_json):
    with open(tickers_json, "r") as read_file:
        data = json.load(read_file)
        extracted_data = transform(data)

        for _row in extracted_data:
            try:
                ins = TicketsTable.insert().values(**_row)

                logging.info(str({_row['cik']:[


                    _row['date_added']
                    ]})+"data inserted into database")
                conn.execute(ins)
                conn.commit()
            except:
                conn.rollback()
                logging.warning(str({_row['cik']:[


                    _row['date_added']
                    ]})+"data could not be inserted into database")
    print("DB update")

if __name__ == '__main__':
    pass