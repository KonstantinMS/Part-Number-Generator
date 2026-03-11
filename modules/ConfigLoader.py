"""
Загрузка конфигурации из YAML файла
"""

import os

import yaml

from .Logger import get_logger

logger = get_logger(__name__)


def load_config(config_path):
    """
    Загружает конфигурацию из YAML файла
    """
    if not os.path.exists(config_path):
        logger.error(f"Файл конфигурации не найден: {config_path}")
        return None

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            logger.info(f"Загружено {config_path}")
        return config

    except yaml.YAMLError as e:
        logger.error(f"Ошибка парсинга YAML: {e}")
        return None

    except Exception as e:
        logger.error(f"Ошибка загрузки конфигурации: {e}")
        return None
