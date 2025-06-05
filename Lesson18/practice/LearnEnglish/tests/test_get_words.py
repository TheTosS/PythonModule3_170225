import pytest
import sqlite3
from pathlib import Path

# Импортируем функции из вашего файла с кодом
from database import init_db, add_word, get_words, Connect



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


def test_get_words_empty_dictionary(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words возвращает пустой словарь и выводит сообщение,
    когда словарь пуст.
    """
    words = get_words(in_memory_cursor)

    assert words == {}, "Функция должна возвращать пустой словарь при отсутствии слов."


def test_get_words_single_word(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words корректно извлекает одно слово.
    """
    add_word("cat", "кошка", in_memory_cursor)
    words = get_words(in_memory_cursor)

    assert words == {"cat": "кошка"}, "Функция должна вернуть словарь с одним словом."


def test_get_words_multiple_words(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words корректно извлекает несколько слов.
    """
    add_word("zebra", "зебра", in_memory_cursor)
    add_word("apple", "яблоко", in_memory_cursor)
    add_word("dog", "собака", in_memory_cursor)

    words = get_words(in_memory_cursor)

    expected_words = {
        "zebra": "зебра",
        "apple": "яблоко",
        "dog": "собака"
    }

    assert words == expected_words, "Функция должна вернуть словарь со всеми добавленными словами."

