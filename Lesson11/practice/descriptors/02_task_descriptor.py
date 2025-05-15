#  Дескриптор-Логгер Изменений (LoggedAttribute)
# Создайте дескриптор, который при каждом чтении или записи атрибута выводит в консоль сообщение о происходящей операции.
# Сам дескриптор управляет хранением значения.
#
# Требования:
# Реализуйте __set_name__.
# Реализуйте __get__. Перед возвратом значения (полученного из словаря экземпляра),
#   выведите сообщение вроде f"Чтение атрибута '{self._public_name}'"
#   Если значение не установлено, верните None или вызовите AttributeError.
# Реализуйте __set__. Перед сохранением значения в словаре экземпляра,
#   выведите сообщение вроде f"Запись в атрибут '{self._public_name}': {value}".
#   Затем сохраните значение.


# Пример использования:
class LoggedAttribute:
    ...  # Ваш код дескриптора


class Settings:
    debug_mode = LoggedAttribute()
    verbose = LoggedAttribute()

    def __init__(self, debug_mode, verbose):
        self.debug_mode = debug_mode
        self.verbose = verbose


# Пример работы:
s = Settings(True, False)  # Вызывает __set__ дважды

print("\n--- Доступ к атрибутам ---")
print(s.debug_mode)  # Вызывает __get__
print(s.verbose)  # Вызывает __get__

print("\n--- Изменение атрибутов ---")
s.debug_mode = False  # Вызывает __set__

print("\n--- Снова доступ ---")
print(s.debug_mode)  # Вызывает __get__
