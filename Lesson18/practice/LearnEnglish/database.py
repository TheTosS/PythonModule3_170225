import random
import sqlite3
from pathlib import Path
from helpers.connection import Connect

DATABASE_NAME = 'vocabulary.db'


def init_db():
    """Инициализирует базу данных, создает таблицу words, если ее нет."""
    sql = """
    CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english_word TEXT NOT NULL UNIQUE,
    russian_translation TEXT NOT NULL
    )
    """
    try:
        with Connect(Path(DATABASE_NAME)) as cursor:
            cursor.execute(sql)
        print("База данных готова.")
    except sqlite3.Error as e:
        print(f"Не удалось инициализировать базу данных: {e}")


def add_word(english_word: str, russian_translation: str) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""
    sql_insert = """INSERT INTO words (english_word, russian_translation) VALUES (?, ?)"""
    try:
        with Connect(Path(DATABASE_NAME)) as cursor:
            cursor.execute(sql_insert, (english_word, russian_translation))
        print("Слово добавлено.")
    except sqlite3.Error as e:
        print(f"Не удалось добавить слово в базу данных: {e}")


def view_words() -> None:
    """Отображает все слова в словаре."""
    sql_select = "SELECT english_word, russian_translation FROM words"
    try:
        with Connect(Path(DATABASE_NAME)) as cursor:
            cursor.execute(sql_select)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"{row[0]} - {row[1]}")
            else:
                print("Словарь пуст.")
    except sqlite3.Error as e:
        print(f"Не удалось получить слова из базы данных: {e}")


def delete_word(english_word: str) -> None:
    """Удаляет слово из словаря по английскому слову."""
    sql_delete = """DELETE FROM words WHERE english_word = ?"""
    with Connect(Path(DATABASE_NAME)) as cursor:
        cursor.execute(sql_delete, (english_word, ))
        if cursor.rowcount == 0:
            print(f"Слово {english_word} в словаре не найдено")
        else:
            print(f"Слово {english_word} удалено!")
