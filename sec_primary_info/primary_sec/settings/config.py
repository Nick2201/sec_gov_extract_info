from pathlib import Path
import json
import sys, os

# Получение текущего пути
current_path = Path.cwd()

# Путь к корневой папке проекта
root_path = current_path.parent.parent

# Используйте root_path для указания пути от корневой папки
# file_path = root_path / "docs"



HOME = Path(__file__)
# TODO: convert to Enum
SETTING_FOLDER = Path(HOME / 'settings')
print(SETTING_FOLDER)

DOCS_FOLDER = Path(HOME / 'docs')
UTILS = Path(HOME / 'utils')
DB_CONFIG_PATH = Path(SETTING_FOLDER / 'db_config.json').absolute()

SRC = Path(HOME / 'src')
TESTS = Path(HOME / 'test')


with open(str(DB_CONFIG_PATH), "r") as read_file:
    DB_CONFIG = json.load(read_file)
    print(DB_CONFIG)

# print(f'FOLDER dor documents is {DOCS_FOLDER}')
# print(Path.cwd())
# print(DOCS_FOLDER)
