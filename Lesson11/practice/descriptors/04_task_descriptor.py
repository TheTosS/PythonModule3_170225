# Описание: Создайте дескриптор, который при присвоении значения атрибуту проверяет,
# что тип присваиваемого значения соответствует определенному типу, указанному при создании дескриптора.

# Требования:
# 1. Дескриптор должен принимать тип данных (int, str, float, и т.д.) в своем конструкторе (__init__).

# 2. Реализуйте __set_name__ для получения имени атрибута.

# 3. Реализуйте __get__ для получения значения из словаря экземпляра.
#   Если значение не установлено, возвращайте None или вызывайте AttributeError

# 4. Реализуйте __set__. В этом методе проверьте, является ли value экземпляром указанного типа
#   (isinstance(value, self.expected_type)).
#   Если нет, вызовите TypeError. Если да, сохраните значение в словаре экземпляра.

# Пример использования:

class TypedAttribute:
    ... # Ваш код дескриптора

class UserSettings:
    user_id = TypedAttribute(int)
    username = TypedAttribute(str)
    rating = TypedAttribute(float)

    def __init__(self, user_id, username, rating):
        self.user_id = user_id    # Проверка типа int
        self.username = username  # Проверка типа str
        self.rating = rating      # Проверка типа float

# Пример работы:
settings = UserSettings(101, "admin", 4.5)
print(settings.user_id)
print(settings.username)
print(settings.rating)

# Попытка присвоить значение некорректного типа
try:
    settings.user_id = "abc" # Ожидается TypeError
except TypeError as e:
    print(f"Ошибка: {e}")

# Попытка присвоить корректное значение
settings.username = "moderator"
print(settings.username)