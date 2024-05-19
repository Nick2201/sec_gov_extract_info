"""

SEC Filing Scraper
@author: AdamGetbags

"""

import yaml
import json
# import modules
import requests
import pandas as pd
with open("etl_config.yaml") as stream:
    try:
        etl_config = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from typing import List, Dict, Any
def extract(): #from
    headers = {'User-Agent': "email@address.com"}


    temp_tickers = requests.get(
        etl_config['source']['extract']['url'],
        headers=headers
        )
  
    return temp_tickers


def transform (df_raw_tickers:pd.DataFrame)->pd.DataFrame:
    '''
        CREATE:
        - cik_str
        - time_load
    '''
    df_raw_tickers['cik_str'] = df_raw_tickers['cik_str'].astype(
                           str).str.zfill(10)
    df_raw_tickers['time_load'] = datetime.today()
    return df_raw_tickers

def load(
        df_repare_to_load:pd.DataFrame,
        connect_string:str)->None:
    # connect_string = etl_config['source']['load']['type']['Database']['test']['url'] #.format(**db)
    engine = create_engine(connect_string)
    df_repare_to_load.to_sql('raw_tickers', con=engine, if_exists='replace')

    return None