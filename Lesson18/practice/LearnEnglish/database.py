import random
import sqlite3
from pathlib import Path
from helpers.connection import Connect

DATABASE_NAME = 'vocabulary.db'


def init_db():
    """Инициализирует базу данных, создает таблицу words, если ее нет."""
    sql = """
    CREATE TABLE ...
    """
    try:
        with Connect(Path(DATABASE_NAME)) as cursor:
            cursor.execute(sql)
        print("База данных готова.")
    except sqlite3.Error as e:
        print(f"Не удалось инициализировать базу данных: {e}")


def add_word(english_word: str, russian_translation: str) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""

    ...


def view_words() -> None:
    """Отображает все слова в словаре."""
    ...


def delete_word(english_word: str) -> None:
    """Удаляет слово из словаря по английскому слову."""
    ...
