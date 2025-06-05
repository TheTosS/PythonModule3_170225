import random
import sqlite3
from pathlib import Path
from helpers.connection import Connect

DATABASE_NAME = 'vocabulary.db'


def init_db(cursor: sqlite3.Cursor):
    """Инициализирует базу данных, создает таблицу words, если ее нет."""
    sql = """
    CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english_word TEXT NOT NULL UNIQUE,
    russian_translation TEXT NOT NULL
    )
    """
    try:
        cursor.execute(sql)
        print("База данных готова.")
    except sqlite3.Error as e:
        print(f"Не удалось инициализировать базу данных: {e}")


def add_word(english_word: str, russian_translation: str, cursor: sqlite3.Cursor) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""
    sql_insert = """INSERT INTO words (english_word, russian_translation) VALUES (?, ?)"""
    try:
        cursor.execute(sql_insert, (english_word, russian_translation))
        print("Слово добавлено.")
    except sqlite3.Error as e:
        print(f"Не удалось добавить слово в базу данных: {e}")
        raise ValueError


def view_words(cursor: sqlite3.Cursor) -> None:
    """Отображает все слова в словаре."""
    sql_select = "SELECT english_word, russian_translation FROM words"
    try:
        cursor.execute(sql_select)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"{row[0]} - {row[1]}")
        else:
            print("Словарь пуст.")
    except sqlite3.Error as e:
        print(f"Не удалось получить слова из базы данных: {e}")


def get_words(cursor: sqlite3.Cursor) -> dict:
    sql = "SELECT english_word, russian_translation FROM words"
    all_words = {}
    cursor.execute(sql)
    rows = cursor.fetchall()
    if not rows:
        print("Словарь пуст. Добавьте слова, для запуска теста.")
        return {}
    else:
        for row in rows:
            all_words[row[0]] = row[1]

    return all_words


def delete_word(english_word: str, cursor: sqlite3.Cursor) -> None:
    """Удаляет слово из словаря по английскому слову."""
    sql_delete = """DELETE FROM words WHERE english_word = ?"""
    cursor.execute(sql_delete, (english_word,))
    if cursor.rowcount == 0:
        print(f"Слово {english_word} в словаре не найдено")
    else:
        print(f"Слово {english_word} удалено!")


def get_all_tables(cursor: sqlite3.Cursor):
    """Вспомогательная функция для получения списка всех таблиц в БД (для тестов)."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]


def get_table_info(cursor: sqlite3.Cursor, table_name: str):
    """Вспомогательная функция для получения информации о таблице (для тестов)."""
    cursor.execute(f"PRAGMA table_info({table_name})")
    return cursor.fetchall()
