import sqlite3

# 1. Подключение к базе данных
conn = sqlite3.connect('products.db')

# 2. Создание объекта курсора
cursor = conn.cursor()

# 3. Обновление количества товара
update_sql = "UPDATE Products SET StockQuantity = ? WHERE ProductName = ?;"
product_name_to_update = 'Монитор 27 дюймов'
new_quantity = 35

cursor.execute(update_sql, (new_quantity, product_name_to_update))
conn.commit() # Сохраняем изменения

print(f"\nОбновлено количество для '{product_name_to_update}'.")

# Проверяем обновление
cursor.execute("SELECT ProductName, StockQuantity FROM Products WHERE ProductName = ?;", (product_name_to_update,))
print(f"Новое количество для '{product_name_to_update}': {cursor.fetchone()}")

# Закрытие соединения
cursor.close()
conn.close()

print("\nСоединение с базой данных закрыто.")