import re # Импортируем модуль для работы с регулярными выражениями

class UserProfile:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        print("Вызван геттер (@property): получение email")
        return self.__email

    @email.setter
    def email(self, value):
        print(f"Вызван сеттер (@email.setter): попытка установить email на '{value}'")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not isinstance(value, str) or not re.match(email_regex, value):
            raise ValueError(f"Некорректный формат email: '{value}'")
        self.__email = value
        print(f"email {value} успешно установлен")


# --- Деail)монстрация использования ---
print("--- Создание профиля пользователя ---")
correct_email = "test.user@example.com"
incorrect_email = "test.user@example"

try:
    user = UserProfile(correct_email)
except ValueError as e:
    print(f"Ошибка при создании: {e}")

user.email = "new.email@example.com"
print(user.email)