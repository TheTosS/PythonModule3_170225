import typing as t


# Для демонстрации, как импортировать типы
# from typing import Any, Optional, Type # Можно так, если не использовать 't'

class NonNegativeInteger:
    def __set_name__(self, owner, name):
        self._private_name = f'_{name}'
        self._public_name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._private_name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Attribute '{self._public_name}' must be an integer.")
        if value < 0:
            raise ValueError(f"Attribute '{self._public_name}' must be non-negative.")
        instance.__dict__[self._private_name] = value


# Пример использования дескриптора
class Product:
    # Создаем экземпляры дескриптора как атрибуты КЛАССА.
    # __set_name__ вызывается автоматически при определении класса.
    quantity = NonNegativeInteger()
    price = NonNegativeInteger()  # Можно использовать один и тот же дескриптор для разных атрибутов

    def __init__(self, name: str, quantity: int, price: int):
        self.name = name
        # Присвоение здесь вызовет __set__ соответствующих дескрипторов
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        # Для удобного вывода экземпляров
        # Попытка чтения здесь может вызвать AttributeError если атрибут удален
        try:
            return f"Product(name='{self.name}', quantity={self.quantity}, price={self.price})"
        except AttributeError as e:
            return f"Product(name='{self.name}', ERROR: {e})"


# Демонстрация работы
print("--- Создание экземпляра и присвоение ---")
try:
    p1 = Product("Banana", 20, 50)
    print(p1)
except (TypeError, ValueError, AttributeError) as e:
    print(f"Ошибка при создании: {e}")

print("\n--- Чтение и изменение значений ---")
try:
    print(f"Исходная цена: {p1.price}")  # Чтение вызывает __get__
    p1.price = 75  # Присвоение вызывает __set__
    print(f"Новая цена: {p1.price}")
except (TypeError, ValueError, AttributeError) as e:
    print(f"Ошибка при чтении/изменении: {e}")

print("\n--- Попытка присвоить некорректные значения ---")
try:
    p1.quantity = -5  # Вызовет __set__, проверка < 0 вызовет ValueError
except ValueError as e:
    print(f"Ошибка при присвоении отрицательного значения: {e}")

try:
    p1.quantity = "много"  # Вызовет __set__, проверка типа вызовет TypeError
except TypeError as e:
    print(f"Ошибка при присвоении некорректного типа: {e}")

