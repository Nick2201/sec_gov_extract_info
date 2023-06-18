

import sys,os
sys.path.insert(0, os.getcwd())
from pathlib import Path
import json
current_path = Path(Path.cwd()/"primary_sec").absolute()
DOCS_FOLDER = Path(current_path/"docs")
SETTINGS_FOLDER= Path(current_path/'settings')

DB_CONFIG_PATH = Path(SETTINGS_FOLDER/"db_config.json")
with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)
    print(DB_CONFIG)



from sqlalchemy import ( create_engine,
    MetaData, Table,Column,
    String, DateTime,Integer)
from sqlalchemy.orm import sessionmaker
from enum import Enum,auto
# import psycopg2
dialect = 'postgresql'
unpack_conf = dialect + '://{user}:{password}@{host}:{port}/{database}'.format(**DB_CONFIG)
"""
       'cik' : 'cik',
        "filed" : "date_publication",
        'quartal',
        'date_added',
        'url_report'

"""
engine = create_engine(unpack_conf)

print(unpack_conf)


metadata = MetaData()
report_liks = Table (
    'report_liks', metadata,
    Column('id', Integer(), primary_key=True),
    Column('cik', String(10)),
    Column('date_publication', DateTime()),
    Column('quartal', String(1)),
    Column('date_added', DateTime()),
    Column('url_report', String(80),unique=True)
)



TicketsTable = Table(
    'tickers_table',metadata,
    Column('id', Integer(), primary_key=True),
    Column('cik', String(10)),                  # if in some do
    Column('ticker', String(10)),
    Column('title', String(120)),
    Column('date_added', DateTime()),
)

conn = engine.connect()
metadata.create_all(engine)


