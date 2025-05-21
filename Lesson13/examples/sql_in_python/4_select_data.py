import sqlite3

# 1. Подключение к базе данных
conn = sqlite3.connect('products.db')

# 2. Создание объекта курсора
cursor = conn.cursor()
# Запрос на получение всех товаров
select_all_sql = "SELECT * FROM Products;"

cursor.execute(select_all_sql)

# 3. Получение результатов
# fetchall() - возвращает все оставшиеся строки запроса как список кортежей.
# fetchone() - возвращает следующую строку запроса как кортеж.
# fetchmany(size) - возвращает указанное количество строк.
rows = cursor.fetchall()

print("\nВсе товары в базе данных:")
for row in rows:
    print(row)  # Каждая строка - это кортеж

# Пример получения товаров с ценой больше 5000
select_filtered_sql = "SELECT ProductName, Price FROM Products WHERE Price > 5000;"
cursor.execute(select_filtered_sql)
filtered_products = cursor.fetchall()

print("\nТовары с ценой > 5000:")
for product in filtered_products:
    print(f"Название: {product[0]}, Цена: {product[1]}")

# Закрытие соединения
cursor.close()
conn.close()

print("\nСоединение с базой данных закрыто.")