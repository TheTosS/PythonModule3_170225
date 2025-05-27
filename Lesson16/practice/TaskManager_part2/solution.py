from connection import Connect
from pathlib import Path
from typing import Optional


class Task:
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    def __init__(self, title, description="", status="Pending", priority=3, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', priority='{self.priority}')"


class TaskRepository:
    DB_FILE = Path("tasks.db")

    def __init__(self):
        TaskRepository._ensure_db_table_exists()

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

    def save(self, task: Task):
        """
        Сохраняет или обновляет задачу в базе данных.
        Если id None, вставляет новую задачу. Иначе, обновляет существующую.
        """
        sql_insert = "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)"
        sql_update = """
            UPDATE tasks 
            SET title = ?, description = ?, status = ?, priority = ?
            WHERE task_id = ?;
        """
        if task.id:
            with Connect(TaskRepository.DB_FILE) as cursor:
                cursor.execute(sql_update, (task.title, task.description, task.status, task.priority, self.id))
        else:
            with Connect(TaskRepository.DB_FILE) as cursor:
                cursor.execute(sql_insert, (task.title, task.description, task.priority))
                task.id = cursor.lastrowid

    def get_by_id(self, id) -> Optional['Task']:
        sql_select = "SELECT * FROM tasks WHERE task_id = ?"
        with Connect(self.DB_FILE) as cursor:
            cursor.execute(sql_select, (id,))
            data = cursor.fetchone()
            if data is None:
                return None
            return Task(*data[1:], data[0])

    def get_all_tasks(self) -> list['Task']:
        sql_select = "SELECT * FROM tasks"
        with Connect(self.DB_FILE) as cursor:
            cursor.execute(sql_select)
            tasks_data = cursor.fetchall()
            tasks = []
            for data in tasks_data:
                tasks.append(Task(*data[1:], data[0]))
            return tasks

    def delete(self, task: Task):
        """Удаляет задачу из базы данных."""
        # TODO-3: реализуйте метод
        if not task.id:
            print(f"нельзя удалить задачу без id")
            return
        sql_delete = "DELETE FROM tasks WHERE task_id = ?"
        with Connect(TaskRepository.DB_FILE) as cursor:
            cursor.execute(sql_delete, (task.id,))
            if cursor.rowcount > 0:
                print(f"Задача с id={task.id} удалена")
                task.id = None
            else:
                print(f"Задача с id={task.id} не найдена")


# Использование
task_repository = TaskRepository()  # Создаем экземпляр репозитория

# Создаем новую задачу
# new_task = Task("Купить молоко", "Зайти в магазин", priority=1)
# task_repository.save(new_task)  # Сохраняем новую задачу, new_task.id будет обновлен

task = task_repository.get_by_id(id=1)
task_repository.delete(task)
print(task)
# print(f"Сохранена новая задача: {new_task}")

# Получаем задачу по ID
# retrieved_task = task_repository.get_by_id(new_task.id)
# if retrieved_task:
#     print(f"Получена задача: {retrieved_task}")
#     retrieved_task.description = "Купить 2 литра молока"
#     retrieved_task.mark_as_in_progress()
#     task_repository.save(retrieved_task)  # Обновляем задачу
#     print(f"Обновленная задача: {retrieved_task}")
#
# # Получаем все задачи
# all_tasks = task_repository.get_all_tasks()
# print("\nВсе задачи:")
# for task in all_tasks:
#     print(task)
#
# # Удаляем задачу
# if retrieved_task:
#     task_repository.delete(retrieved_task)
#     print(task_repository.get_by_id(retrieved_task.id))  # Должно быть None
