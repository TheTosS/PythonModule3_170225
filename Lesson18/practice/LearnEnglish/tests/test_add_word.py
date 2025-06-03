import pytest
import sqlite3
from pathlib import Path
from database import init_db

# Импортируем функции из вашего основного файла приложения
# Убедитесь, что main_app.py находится в том же каталоге или в PYTHONPATH
from helpers.connection import Connect

@pytest.fixture
def in_memory_db():
    """
    Фикстура Pytest для создания временной (in-memory) базы данных SQLite
    для каждого теста.
    """
    db_path = Path(":memory:")  # Специальный путь для in-memory DB
    init_db(db_path) # Инициализируем структуру таблицы
    return db_path