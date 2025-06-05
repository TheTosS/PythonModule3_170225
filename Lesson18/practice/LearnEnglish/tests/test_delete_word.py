import pytest
import sqlite3
from pathlib import Path

# Импортируем только нужные функции из вашего файла с кодом
from database import init_db, add_word, delete_word

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
        init_db(cursor)  # Используем init_db для создания таблицы

        yield cursor  # Возвращаем курсор для использования в тестах

    finally:
        # Этот блок выполняется после завершения каждого теста
        if conn:
            conn.commit()  # Сохраняем все изменения, сделанные в тесте
            conn.close()  # Закрываем соединение, уничтожая in-memory БД


def test_delete_word_success(in_memory_cursor):
    """
    Тест: Успешное удаление существующего слова.
    """
    add_word("apple", "яблоко", in_memory_cursor)

    # Получаем начальное количество слов
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    initial_count = in_memory_cursor.fetchone()[0]

    delete_word("apple", in_memory_cursor)

    # Проверяем, что слово удалено
    in_memory_cursor.execute("SELECT russian_translation FROM words WHERE english_word = ?", ("apple",))
    assert in_memory_cursor.fetchone() is None

    # Проверяем, что количество слов уменьшилось на 1
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == initial_count - 1


def test_delete_word_not_found(in_memory_cursor, capsys):
    """
    Тест: Попытка удалить несуществующее слово.
    Проверяем, что база данных не изменилась.
    """
    add_word("banana", "банан", in_memory_cursor)

    # Получаем начальное количество слов
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    initial_count = in_memory_cursor.fetchone()[0]

    delete_word("nonexistent_word", in_memory_cursor)

    # Проверяем, что количество слов не изменилось
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == initial_count

    # Проверяем, что исходное слово осталось
    in_memory_cursor.execute("SELECT russian_translation FROM words WHERE english_word = ?", ("banana",))
    assert in_memory_cursor.fetchone()[0] == "банан"


def test_delete_word_empty_string(in_memory_cursor, capsys):
    """
    Тест: Попытка удалить слово с пустой строкой.
    """
    add_word("test", "тест", in_memory_cursor)

    # Получаем начальное количество слов
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    initial_count = in_memory_cursor.fetchone()[0]

    delete_word("", in_memory_cursor)

    # Убеждаемся, что ничего не удалилось
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == initial_count

    in_memory_cursor.execute("SELECT russian_translation FROM words WHERE english_word = ?", ("test",))
    assert in_memory_cursor.fetchone()[0] == "тест"


def test_delete_word_case_insensitivity(in_memory_cursor):
    """
    Тест: Удаление слова должно быть регистронезависимым.
    """
    add_word("Keyboard", "клавиатура", in_memory_cursor)

    # Получаем начальное количество слов
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    initial_count = in_memory_cursor.fetchone()[0]

    delete_word("keyboard", in_memory_cursor)  # Удаляем с другим регистром

    in_memory_cursor.execute("SELECT russian_translation FROM words WHERE english_word = ?", ("keyboard",))
    assert in_memory_cursor.fetchone() is None

    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == initial_count - 1
