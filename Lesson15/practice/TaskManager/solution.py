from connection import Connect
from pathlib import Path


class Task:
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    DB_FILE = Path("tasks.db")

    def __init__(self, title, description="", priority="Pending"):
        # TODO-0: что будем делать с id?
        self.id = ...
        self.title = title
        self.description = description
        self.priority = priority

    @classmethod
    def _ensure_db_table_exists(cls):
        """Создает таблицу tasks, если она еще не существует."""
        # cls.DB_FILE.parent.mkdir(parents=True, exist_ok=True)  # Убедимся, что директория существует
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tasks
                    (
                        task_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                        title       TEXT NOT NULL,
                        description TEXT,
                        status      TEXT CHECK (status IN ('Pending', 'In Progress', 'Completed')) DEFAULT 'Pending',
                        priority    INTEGER CHECK ( priority BETWEEN 1 AND 5) DEFAULT 3
                    );
                ''')
        # commit() происходит автоматически при выходе из with Connect

    def __repr__(self):
        # TODO-1: Возвращает строку формата Task(id=..., title='...', priority=...)
        ...

    def save(self):
        """
        Сохраняет или обновляет задачу в базе данных.
        Если id None, вставляет новую задачу. Иначе, обновляет существующую.
        """
        # TODO-2: реализуйте метод
        sql_insert = "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)"

    def load(self):
        """
        Загружает задачу из БД
        """
        # TODO-4: реализуйте метод

    def delete(self):
        """Удаляет задачу из базы данных."""
        # TODO-3: реализуйте метод
