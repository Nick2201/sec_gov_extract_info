from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict, Any



import json
from pymongo import command_cursor,collection
from pathlib import Path
import sys
from icecream import ic
import pandas as pd
current_dir = (Path(__file__).parent.parent.parent)
models_file = Path(current_dir/'credentials.json')
sys.path.append(str(models_file))

with open(models_file) as config_file: 
    config: Dict =  json.loads(config_file.read())

print(config['test'])

# +asyncpg

connection:str = f"{'dialect'}://{'user'}:{'psw'}@{'host'}:{'port'}/{'db'}".format(**config['test'])
ic(connection)
# connection:str = f"{'dialect'}://{'user'}:{'psw'}@{'host'}:{'port'}/{'db'}".format(**config['dw'])
# ic(connection)
print(connection)

tickers_table:str = 'tickers'
pd.read_sql(f"select * from {tickers_table}", connection)


class IConnector(ABC):
    @abstractmethod
    def connect(self) -> Dict[str, Any]:
        
        print(self.config)
        pass

'''
    async
    Connector:
        - mongo
        - postgres
'''


@dataclass(frozen=True)
class Connector:
    config: Dict[str, Any]

    def connect(self):

        pass


@dataclass
class Extract:
    # connectror:
    ...


@dataclass
class Transform:
    ... 

@dataclass
class Load:
    ...

