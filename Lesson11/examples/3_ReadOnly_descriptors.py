import typing as t


class ReadOnly:
    """
    Дескриптор для создания атрибута только для чтения после первой установки.
    """

    def __set_name__(self, owner: type, name: str) -> None:
        self._private_name = f'_{name}'
        self._public_name = name

    def __get__(self, instance: t.Optional[object], owner: type) -> t.Any:
        # Получаем значение из словаря экземпляра.
        # Поднимаем AttributeError, если значение еще не установлено.
        try:
            return instance.__dict__[self._private_name]
        except KeyError:
            raise AttributeError(f"Атрибут '{self._public_name}' еще не установлен.")

    def __set__(self, instance: object, value: t.Any) -> None:
        # Проверяем, было ли значение уже установлено
        if self._private_name in instance.__dict__:
            raise AttributeError(f"Атрибут '{self._public_name}' является только для чтения и уже установлен.")

        # Если не установлено, сохраняем значение
        instance.__dict__[self._private_name] = value


# Пример использования:
class ImmutablePoint:
    x = ReadOnly()  # Атрибут x будет только для чтения
    y = ReadOnly()  # Атрибут y будет только для чтения

    def __init__(self, x: int, y: int):
        # Значения устанавливаются здесь, вызывая __set__ дескрипторов
        self.x = x
        self.y = y
        # После этой точки атрибуты x и y станут только для чтения

    def __repr__(self) -> str:
        # Чтение атрибутов здесь вызывает __get__ дескрипторов
        return f"ImmutablePoint(x={self.x}, y={self.y})"


# Демонстрация:
point = ImmutablePoint(10, 20)
print(point)  # Вывод: ImmutablePoint(x=10, y=20) (чтение вызывает __get__)

try:
    point.x = 30  # Попытка изменить - вызовет __set__ и ошибку
except AttributeError as e:
    print(f"Ошибка при изменении x: {e}")  # Ожидаемый вывод: AttributeError: Attribute 'x' is read-only...
