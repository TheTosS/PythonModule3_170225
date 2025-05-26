from connection import Connect
from pathlib import Path


class Task:
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    DB_FILE = Path("tasks.db")

    def __init__(self, title, description="", status="Pending", priority=3):
        self.id = None
        self.title = title
        self.description = description
        self.status = status
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
        return f"Task(id={self.id}, title='{self.title}', priority='{self.priority}')"

    def save(self):
        """
        Сохраняет или обновляет задачу в базе данных.
        Если id None, вставляет новую задачу. Иначе, обновляет существующую.
        """
        Task._ensure_db_table_exists()
        # TODO-2(complete): реализуйте метод
        sql_insert = "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)"
        sql_update =  """
            UPDATE tasks 
            SET title = ?, description = ?, status = ?, priority = ?
            WHERE task_id = ?;
        """
        if self.id:
            with Connect(Task.DB_FILE) as cursor:
                cursor.execute(sql_update, (self.title, self.description, self.status, self.priority, self.id))
        else:
            with Connect(Task.DB_FILE) as cursor:
                cursor.execute(sql_insert, (self.title, self.description, self.priority))
                self.id = cursor.lastrowid


    def load(self):
        """
        Загружает задачу из БД
        """
        # TODO-4: реализуйте метод

    def delete(self):
        """Удаляет задачу из базы данных."""
        # TODO-3: реализуйте метод


task1 = Task("тестовая задача")
task1.save() # -> DB
task1.priority = 1
task1.save() # -> UPDATE
task1.save()
task1.save()