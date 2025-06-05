import pytest
import sqlite3
from pathlib import Path
from database import init_db, get_all_tables, get_table_info

from helpers.connection import Connect


@pytest.fixture
def db_cursor():
    """
    Фикстура Pytest, которая создает и предоставляет курсор к базе данных SQLite в памяти.
    Это гарантирует, что все операции в тесте используют одно и то же соединение.
    """
    db_conn_obj = Connect(Path(":memory:"))
    with db_conn_obj as cursor:
        yield cursor


def test_init_db_creates_table(db_cursor):  # <--- Теперь фикстура предоставляет cursor
    """
    Тест: Убедиться, что init_db создает таблицу 'words'.
    """
    # Вызываем функцию, которую тестируем, передавая ей cursor из фикстуры
    init_db(db_cursor)

    # Проверяем, что таблица 'words' существует, используя тот же cursor
    tables = get_all_tables(db_cursor)
    assert 'words' in tables, "Таблица 'words' должна быть создана."


def test_init_db_creates_correct_columns(db_cursor):  # <--- Принимает cursor
    """
    Тест: Убедиться, что таблица 'words' имеет правильные колонки.
    """
    init_db(db_cursor)
    columns_info = get_table_info(db_cursor, 'words')

    column_names = [col[1] for col in columns_info]
    column_types = {col[1]: col[2] for col in columns_info}

    assert 'id' in column_names
    assert 'english_word' in column_names
    assert 'russian_translation' in column_names

    assert column_types['id'] == 'INTEGER'
    assert column_types['english_word'] == 'TEXT'
    assert column_types['russian_translation'] == 'TEXT'


