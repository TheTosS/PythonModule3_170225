import sqlite3


class Connect:
    """
    Класс для подключения к базе данных SQLite,
    поддерживающий использование с оператором 'with'.
    """

    def __init__(self, db_name:str):
        """
        Инициализирует объект Connect.

        Args:
            db_name: Имя файла базы данных SQLite.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self) -> sqlite3.Cursor:
        """
        Метод, вызываемый при входе в контекстный менеджер 'with'.
        Устанавливает соединение с базой данных и создает курсор.

        Returns:
            sqlite3.Cursor: Объект курсора для выполнения SQL-запросов.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return self.cursor
        except sqlite3.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")
            # Возможно, стоит перебросить исключение или выполнить другую обработку ошибки
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, вызываемый при выходе из контекстного менеджера 'with'.
        Закрывает соединение с базой данных.

        Args:
            exc_type: Тип исключения (если оно было).
            exc_val: Значение исключения.
            exc_tb: Объект трассировки исключения.
        """
        if self.conn:
            if exc_type is None:
                # Если исключений не было, сохраняем изменения
                self.conn.commit()
            else:
                # Если было исключение, откатываем изменения
                self.conn.rollback()
                print(f"Произошла ошибка: {exc_val}. Изменения откачены.")
            self.conn.close()


# Пример использования:

if __name__ == "__main__":
    db_file = "my_database.db"

    # Создание таблицы и вставка данных
    try:
        with Connect(db_file) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )
            ''')
            cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
            cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
            print("Таблица 'users' создана и данные вставлены.")
    except Exception as e:
        print(f"Ошибка при работе с базой данных: {e}")

    # Чтение данных
    try:
        with Connect(db_file) as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print("\nДанные из таблицы 'users':")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")

    # Пример с ошибкой (для демонстрации rollback)
    print("\nПопытка вставки некорректных данных (вызовет ошибку):")
    try:
        with Connect(db_file) as cursor:
            # Нарушение NOT NULL ограничения для name
            cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (None, 40))
            print("Эта строка не должна быть выведена, так как будет ошибка.")
    except Exception as e:
        print(f"Обнаружена ошибка при вставке: {e}")
        print("Изменения должны быть отменены.")

    # Проверка, что некорректные данные не были добавлены
    try:
        with Connect(db_file) as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print("\nДанные из таблицы 'users' после попытки ошибочной вставки:")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
