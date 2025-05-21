class Task:
    id = 1
    text = "..."
    status = "В процессе"/ "Выполнена"

    def change_status(self, new_status) -> None:
        ...


class Manager:
    tasks = []

    def add_task(self, task: Task) -> None:
        ...

    def find_task_by_id(self, id: int) -> Task| None:
        ...

    def get_tasks_by_status(self, status: str) -> list[Task]:
        ...

    def get_all_tasks(self) -> list[Task]:
        ...

    def load_from_file(self, file_name) -> None:
        ...

    def save_to_file(self, file_name) -> None:
        ...