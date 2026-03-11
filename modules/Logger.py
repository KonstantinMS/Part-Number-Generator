# logger.py
import logging
import os
from datetime import datetime


class SimpleLogger:
    def __init__(self, name="app", log_dir="logs", level=logging.INFO):
        """
        Инициализация логгера

        Args:
            name: имя логгера
            log_dir: директория для логов
            level: уровень логирования
        """
        self.name = name
        self.log_dir = log_dir

        # Создаем директорию для логов, если её нет
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Имя файла с датой
        log_file = os.path.join(
            log_dir, f'{name}_{datetime.now().strftime("%Y%m%d")}.log'
        )

        # Настройка логгера
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Очищаем старые обработчики, если есть
        if self.logger.handlers:
            self.logger.handlers.clear()

        # Формат логов
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Обработчик для файла
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Обработчик для консоли
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# Глобальный экземпляр логгера (будет создан при первом импорте)
_logger_instance = None


def get_logger(name="app", log_dir="logs", level=logging.INFO):
    """
    Функция для получения экземпляра логгера (синглтон)
    """
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = SimpleLogger(name, log_dir, level)
    return _logger_instance


# Удобные функции для быстрого логирования
def log_debug(msg):
    get_logger().debug(msg)


def log_info(msg):
    get_logger().info(msg)


def log_warning(msg):
    get_logger().warning(msg)


def log_error(msg):
    get_logger().error(msg)


def log_critical(msg):
    get_logger().critical(msg)
