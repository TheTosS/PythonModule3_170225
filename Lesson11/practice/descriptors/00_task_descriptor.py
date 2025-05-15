# "Дескриптор для Числа в Диапазоне (BoundedNumber)"

# Создайте дескриптор для числовых атрибутов (целые или с плавающей точкой), который гарантирует, что присваиваемое значение находится в заданном диапазоне [минимальное, максимальное].
#
# Требования:
#
# Дескриптор должен принимать min_value и max_value в своем конструкторе __init__.
# Реализуйте __set_name__.
# Реализуйте __get__ (логика та же, что в Задании 1).
# Реализуйте __set__. В этом методе сначала проверьте, является ли value числом (isinstance(value, (int, float))).
#   Если нет, вызовите TypeError. Затем проверьте, что self.min_value <= value <= self.max_value.
#   Если нет, вызовите ValueError. Если проверки пройдены, сохраните значение.
#
# Пример использования:

class BoundedNumber:
     ... # Ваш код дескриптора

class GameStats:
    health = BoundedNumber(0, 100) # Здоровье от 0 до 100
    level = BoundedNumber(1, 50)   # Уровень от 1 до 50

    def __init__(self, health, level):
        self.health = health
        self.level = level

# Пример работы:
stats = GameStats(85, 15)
print(stats.health)
print(stats.level)

# Попытка присвоить значения вне диапазона
try:
    stats.health = 120 # Ожидается ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    stats.level = 0 # Ожидается ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

# Попытка присвоить значение некорректного типа
try:
     stats.health = "max" # Ожидается TypeError
except TypeError as e:
     print(f"Ошибка: {e}")