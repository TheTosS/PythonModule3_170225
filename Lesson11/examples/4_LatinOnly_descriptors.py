import re
import typing as t


class LatinString:
    """
    Дескриптор, обеспечивающий, что атрибут является строкой
    и содержит только латинские буквы (a-z, A-Z).
    """
    # Компилируем регулярное выражение один раз для эффективности
    _latin_only_pattern = re.compile(r'^[a-zA-Z]*$')

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Вызывается при назначении дескриптора атрибуту в классе-владельце.
        Сохраняет имя атрибута для внутреннего использования.
        """
        self._private_name = f'_{name}'  # Имя для хранения в словаре экземпляра
        self._public_name = name  # Публичное имя атрибута

    def __get__(self, instance: t.Optional[object], owner: type) -> t.Optional[str]:
        """
        Вызывается при чтении атрибута.
        Возвращает значение из словаря экземпляра или None, если не установлено.
        """
        # Возвращаем значение из словаря экземпляра.
        # .get(key, default=None) вернет None, если ключ не найден.
        return instance.__dict__.get(self._private_name)

    def __set__(self, instance: object, value: str) -> None:
        """
        Вызывается при записи в атрибут.
        Выполняет проверку типа и содержимого.
        """
        # Проверка типа: должно быть строкой
        if not isinstance(value, str):
            raise TypeError(
                f"Атрибут '{self._public_name}' должен быть строкой, "
                f"получено {type(value).__name__}."
            )

        # Проверка содержимого: только латинские буквы
        # fullmatch() проверяет, соответствует ли ВСЯ строка шаблону
        if not self._latin_only_pattern.fullmatch(value):
            raise ValueError(
                f"Атрибут '{self._public_name}' может содержать только латинские буквы (a-z, A-Z), "
                f"получено '{value}'."
            )

        # Если проверки пройдены, сохраняем значение в словаре экземпляра
        instance.__dict__[self._private_name] = value


# Пример использования:
class UserProfile:
    # Атрибуты first_name и last_name будут управляться дескриптором LatinString
    first_name = LatinString()
    last_name = LatinString()

    def __init__(self, first_name: str, last_name: str):
        # Присвоение здесь вызывает __set__ соответствующих дескрипторов
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        # Чтение здесь вызывает __get__ дескрипторов
        # Используем .get(key) на __dict__ дескриптора для безопасного доступа
        # Или можно просто читать self.attribute_name, и __get__ дескриптора вернет None
        return (
            f"UserProfile("
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}'"
            f")"
        )


# --- Демонстрация работы ---

print("--- Создание экземпляра с корректными данными ---")
try:
    user1 = UserProfile("Alice", "Smith")
    print(user1)
except (TypeError, ValueError, AttributeError) as e:
    print(f"Ошибка при создании: {e}")

print("\n--- Попытка присвоить некорректные данные ---")
try:
    user1.first_name = "Алиса"  # Содержит кириллицу
except (TypeError, ValueError) as e:
    print(f"Ошибка при присвоении кириллицы: {e}")  # Ожидаемый вывод: ValueError

try:
    user1.last_name = "Smith123"  # Содержит цифры
except (TypeError, ValueError) as e:
    print(f"Ошибка при присвоении с цифрами: {e}")  # Ожидаемый вывод: ValueError

try:
    user1.first_name = 123  # Не строка
except (TypeError, ValueError) as e:
    print(f"Ошибка при присвоении не строки: {e}")  # Ожидаемый вывод: TypeError

print("\n--- Чтение после ошибок (значения не изменились) ---")
print(user1)  # Значения должны быть исходными: Alice Smith
