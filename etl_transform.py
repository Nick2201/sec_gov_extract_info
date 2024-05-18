# data = facts['us-gaap']
import re
import numpy as np

def normalize_name(name: str) -> str:
    return ' '.join(re.findall('[A-Z][^A-Z]*', name)).lower()

# Функция для извлечения текста из скобок
def extract_description(description: str) -> str:
    if isinstance(description, str):
        match = re.search(r'\(.*?\)', description)
        if match:
            return match.group(0).strip('()')
    return description

def remove_text_in_parentheses(description: str) -> str:
    if isinstance(description, str):
        return re.sub(r'\(.*?\)', '', description).strip()
    return description
# Функция для подготовки колонок
def prepare_columns(data: dict) -> dict:
    columns = {
        'form_name': [],
        'description': [],
        'units': [],
        'form_name_norm': [],
        'description_norm': []
    }

    for key, value in data.items():
        columns['form_name'].append(key)
        description_value = value.get('description', '')
        columns['description'].append(description_value)
        columns['units'].append(", ".join(value['units'].keys()))  # Преобразование ключей словаря в строку
        columns['form_name_norm'].append(normalize_name(key))
        columns['description_norm'].append(remove_text_in_parentheses(description_value))
    
    return columns

# Функция для преобразования колонок в numpy array
def columns_to_numpy(columns: dict) -> np.ndarray:
    return np.array([columns[key] for key in columns])

def transform(data):
    return 
# Подготовка колонок
# columns = prepare_columns(data)

# # Вывод DataFrame
# df4
