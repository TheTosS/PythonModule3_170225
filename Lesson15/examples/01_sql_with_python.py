import sqlite3
from pathlib import Path

# --- 1. Определение пути к файлу БД с помощью pathlib ---
DB_DIR = Path("./data")  # Директория для базы данных
DB_FILE = DB_DIR / "simple_db.db"  # Полный путь к файлу БД

# Создаем директорию, если она не существует
DB_DIR.mkdir(exist_ok=True)

conn = None  # Инициализируем переменную для соединения

try:
    print(f"Подключаемся к базе данных: {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    print("Соединение с базой данных установлено.")

    # --- 1. Успешная операция: Создание таблицы и вставка данных ---
    print("Создаем таблицу 'users' и вставляем корректные данные...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT
        )
    ''')
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("alice_wonder", "alice@example.com"))
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("bob_builder", "bob@example.com"))
    conn.commit()  # Фиксируем изменения
    print("Данные 'alice_wonder' и 'bob_builder' успешно вставлены и зафиксированы.")

    # --- 2. Некорректная операция: Попытка вставки дубликата (rollback) ---
    print("\n--- Демонстрация некорректной операции (rollback) ---")
    try:
        print("Попытка вставки дубликата пользователя 'alice_wonder'")
        # Эта вставка нарушит ограничение UNIQUE для username
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("alice_wonder", "alice_new@example.com"))
        conn.commit()  # Эта строка не будет достигнута, если возникнет ошибка
        print("Некорректные данные вставлены (это не должно произойти).")
    except sqlite3.IntegrityError as e:
        print(f"ОШИБКА: Произошла ошибка целостности данных: {e}")
        conn.rollback()  # Откатываем все изменения в текущей транзакции
        print("Изменения откачены (rollback) из-за ошибки UNIQUE.")
    except sqlite3.Error as e:
        print(f"ОШИБКА: Произошла общая ошибка SQLite: {e}")
        conn.rollback()
        print("Изменения откачены (rollback) из-за общей ошибки.")

    # --- 4. Проверка состояния БД после отката ---
    print("\nПроверяем записи после попытки ошибочной вставки (дубликата быть не должно):")
    cursor.execute("SELECT * FROM users")
    final_rows = cursor.fetchall()
    for row in final_rows:
        print(row)
    if len(final_rows) == 2:  # Ожидаем только 2 записи
        print("Количество записей осталось прежним (2), что подтверждает успешный откат.")

except sqlite3.Error as e:
    print(f"Критическая ошибка базы данных вне блока try для ошибок: {e}")
    if conn:
        conn.rollback()  # Откатываем изменения, если произошла ошибка до первого коммита
        print("Все изменения были откачены из-за критической ошибки.")
finally:
    if conn:
        conn.close()
        print(f"\nСоединение с базой данных '{DB_FILE}' закрыто.")
