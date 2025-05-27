from connection import Connect
from pathlib import Path


class Task:
    # TODO-0: используйте результат предыдущего занятия
    #  следуя принципам SPR, разбейте класс на два:
    #  1. класс Task будет содержать только данные задачи и базовые методы для представления.
    #  2. класс TaskRepository будет отвечать за все операции с базой данных: создание таблицы, сохранение...
    ...

class TaskRepository:
    ...


# Использование
task_repository = TaskRepository() # Создаем экземпляр репозитория

# Создаем новую задачу
new_task = Task("Купить молоко", "Зайти в магазин", priority=1)
task_repository.save(new_task) # Сохраняем новую задачу, new_task.id будет обновлен

# print(f"Сохранена новая задача: {new_task}")

# Получаем задачу по ID
retrieved_task = task_repository.get_by_id(new_task.id)
if retrieved_task:
    print(f"Получена задача: {retrieved_task}")
    retrieved_task.description = "Купить 2 литра молока"
    retrieved_task.mark_as_in_progress()
    task_repository.save(retrieved_task) # Обновляем задачу
    print(f"Обновленная задача: {retrieved_task}")

# Получаем все задачи
all_tasks = task_repository.get_all_tasks()
print("\nВсе задачи:")
for task in all_tasks:
    print(task)

# Удаляем задачу
if retrieved_task:
    task_repository.delete(retrieved_task)
    print(task_repository.get_by_id(retrieved_task.id)) # Должно быть None