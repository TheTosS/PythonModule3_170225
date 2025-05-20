import sqlite3

# 1. Подключение к базе данных
conn = sqlite3.connect('products.db')

# 2. Создание объекта курсора
cursor = conn.cursor()

# Запросы на добавление товаров
insert_data_sql = """
INSERT INTO Products (ProductName, Price, StockQuantity) VALUES
('Монитор 27 дюймов', 18500.00, 30),
('Веб-камера Full HD', 2100.50, 80),
('Наушники Bluetooth', 3500.00, 150),
('Внешний жесткий диск 1ТБ', 5800.00, 45),
('Роутер Wi-Fi AX1800', 3200.00, 60);
"""

try:
    cursor.execute(insert_data_sql)
    conn.commit() # Сохраняем изменения
    print("Данные успешно добавлены.")
except sqlite3.IntegrityError as e:
    print(f"Ошибка при добавлении данных: {e}")

# Закрытие соединения
cursor.close()
conn.close()

print("\nСоединение с базой данных закрыто.")