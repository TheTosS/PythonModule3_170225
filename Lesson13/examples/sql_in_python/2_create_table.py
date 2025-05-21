import sqlite3

# 1. Подключение к базе данных
conn = sqlite3.connect('products.db')

# 2. Создание объекта курсора
cursor = conn.cursor()

# Запрос на создание таблицы
create_table_sql = """
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Price REAL NOT NULL,
    StockQuantity INTEGER DEFAULT 0
);
"""

# 3. Выполнение запроса
cursor.execute(create_table_sql)

# 4. Сохранение изменений (коммит)
# Это необходимо для команд DDL (CREATE, ALTER, DROP)
# и DML (INSERT, UPDATE, DELETE), чтобы изменения вступили в силу.
conn.commit()

print("Таблица 'Products' проверена/создана.")

# Закрытие соединения
cursor.close()
conn.close()

print("\nСоединение с базой данных закрыто.")