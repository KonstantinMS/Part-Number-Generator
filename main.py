#!/usr/bin/env python3
"""
Генератор артикулов конденсаторов Yageo серии CC
"""

import sys

from modules.ConfigLoader import load_config
from modules.Logger import get_logger, log_error, log_info
from modules.PartGenerator import *
from modules.Writer import write_to_excel


def main():
    logger = get_logger("Part Number Generator", level=20)

    # Загрузка конфигурации
    config = load_config("configs/config.yaml")

    if not config:
        log_error("Ошибка загрузки конфигурации")
        sys.exit(1)

    # Генерация артикулов
    part_numbers = [{"ManufacturerPartNumber": "CC0402KRX7R9BB104"}]

    # Сохранение в CSV
    write_to_excel(part_numbers, "generated/C_YAGEO.xlsx")


if __name__ == "__main__":
    main()
