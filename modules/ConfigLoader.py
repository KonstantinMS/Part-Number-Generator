"""
Загрузка конфигурации из YAML файла
"""

import os

import yaml


def load_config(config_path):
    """
    Загружает конфигурацию из YAML файла
    """
    if not os.path.exists(config_path):
        print(f"Файл конфигурации не найден: {config_path}")
        return None

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            print(f"Загружено {config_path}")
        return config

    except yaml.YAMLError as e:
        print(f"Ошибка парсинга YAML: {e}")
        return None

    except Exception as e:
        print(f"Ошибка загрузки конфигурации: {e}")
        return None
