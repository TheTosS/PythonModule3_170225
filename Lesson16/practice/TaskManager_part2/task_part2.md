## Доработка класса Task
1. Добавьте методы для изменения статуса
    * **mark_as_completed**(self): Устанавливает self.status = Task.COMPLETED.
    * **mark_as_in_progress**(self): Устанавливает self.status = Task.IN_PROGRESS. 
    * **mark_as_pending**(self): Устанавливает self.status = Task.PENDING.
2. Добавьте метод для изменения приоритета **set_priority**(self, new_priority: int)

## Доработка класса TaskRepository
1. Методы получения задач с фильтрацией:
   * **get_tasks_by_status**(self, status: str) -> list[Task]: Возвращает список задач с определенным статусом.
   * **get_tasks_by_priority**(self, priority: int) -> list[Task]: Возвращает список задач с определенным приоритетом.
   * **get_completed_tasks**(self) -> list[Task]: Специализированный метод для получения всех завершенных задач.
   * **get_tasks_by_title_contains**(self, keyword: str) -> list[Task]: Поиск задач по ключевому слову в заголовке.
   * **get_tasks_by_priority_range**(self, min_priority: int, max_priority: int) -> list[Task]: Задачи в заданном диапазоне приоритетов.
2. Методы получения задач с сортировкой:
   * **get_all_tasks_sorted_by_priority**(self, ascending: bool = True) -> list[Task]: Получает все задачи, отсортированные по приоритету.
   * **get_tasks_by_status_sorted_by_priority**(self, status: str, ascending: bool = True) -> list[Task]: Получает задачи по статусу, отсортированные по приоритету.
3. Методы пакетных операций:
    * **delete_completed_tasks**(self): Удаляет все задачи со статусом "Завершено".