# Дескриптор для Валидации Email (EmailAttribute)
# Создайте дескриптор, который проверяет, является ли присваиваемая строка адресом электронной почты.

# Требования:
# Реализуйте __set_name__.
# Реализуйте __get__ (логика та же, что в Задании 1).
# Реализуйте __set__.

# Пример использования:
import re

class EmailAttribute:
    def __init__(self):
        self._email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    def __set_name__(self, owner, name):
        self._private_name = f'_{name}'
        self._public_name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._private_name)

    def __set__(self, instance, value):
        if not self._email_pattern.fullmatch(value):
            raise ValueError("email incorrect")
        instance.__dict__[self._private_name] = value


class Contact:
    email = EmailAttribute()

    def __init__(self, email):
        self.email = email


# Пример работы:
contact = Contact("test@example.com")
print(contact.email)

# Попытка присвоить некорректные email-ы
try:
    contact.email = "invalid-email"  # Нет @
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    contact.email = "user@domain@com"  # Два @
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    contact.email = "user @example.com"  # Содержит пробел
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    contact.email = 123  # Не строка
except TypeError as e:
    print(f"Ошибка: {e}")

# Корректное присвоение после ошибок
contact.email = "another.test@sub.example.co.uk"
print(contact.email)
