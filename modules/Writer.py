import os

import pandas as pd

from .Logger import get_logger

logger = get_logger(__name__)


def write_to_excel(parts, output_file):
    """
    Функция для записи в Excel
    """
    # Проверка и создание директории, если её нет
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Создана директория: {output_dir}")

    # Проверка расширения файла
    if not output_file.lower().endswith((".xlsx", ".xls")):
        output_file += ".xlsx"
        logger.info(f"Добавлено расширение .xlsx: {output_file}")

    try:
        df = pd.DataFrame(parts)
        df.to_excel(output_file, index=False)
        return True
    except ImportError:
        print("Для записи в Excel установите pandas: pip install pandas")
        return False
    except Exception as e:
        print(f"Ошибка записи в Excel: {e}")
        return False
