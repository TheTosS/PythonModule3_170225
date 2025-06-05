import pytest
import sqlite3
from pathlib import Path
from unittest.mock import patch

# Импортируем нужные функции из вашего файла с кодом
from database import init_db, add_word, view_words, Connect


@pytest.fixture
def in_memory_cursor():
    """
    Фикстура Pytest, которая создает и инициализирует
    соединение с базой данных SQLite в памяти,
    и возвращает курсор для этого соединения.
    Гарантирует, что таблица 'words' существует и соединение
    корректно закрывается после теста.
    """
    db_path = Path(":memory:")  # Специальное имя для in-memory БД
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Инициализируем таблицу 'words'
        init_db(cursor)

        yield cursor  # Возвращаем курсор для использования в тестах

    finally:
        # Этот блок выполняется после завершения каждого теста
        if conn:
            conn.commit()  # Сохраняем все изменения, сделанные в тесте
            conn.close()  # Закрываем соединение, уничтожая in-memory БД


def test_view_words_empty_dictionary(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что view_words корректно обрабатывает пустой словарь.
    """
    view_words(in_memory_cursor)
    captured = capsys.readouterr()
    assert "Словарь пуст." in captured.out.strip()
    assert captured.err == ""


def test_view_words_single_word(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что view_words корректно отображает одно слово.
    """
    add_word("cat", "кошка", in_memory_cursor)
    view_words(in_memory_cursor)
    captured = capsys.readouterr()
    assert "cat - кошка" in captured.out.strip()
    assert captured.err == ""
