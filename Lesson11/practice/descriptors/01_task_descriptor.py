# Дескриптор для Непустой Строки (NonEmptyString)
# Создайте дескриптор, который гарантирует, что присваиваемое значение является строкой,
# и эта строка не является пустой после удаления начальных и конечных пробелов.
#
# Требования:
#
# Реализуйте __set_name__.
# Реализуйте __get__ (логика та же, что в Задании 1).
# Реализуйте __set__. В этом методе сначала проверьте, является ли value строкой.
#   Если нет, вызовите TypeError. Затем создайте stripped_value = value.strip().
#   Проверьте, что len(stripped_value) > 0. Если строка пуста после удаления пробелов, вызовите ValueError.
#   Если проверки пройдены, сохраните обрезанное (stripped_value) значение.


# Пример использования:

class NonEmptyString:
    ...  # Ваш код дескриптора


class Comment:
    author = NonEmptyString()
    text = NonEmptyString()

    def __init__(self, author, text):
        self.author = author
        self.text = text


# Пример работы:
comment = Comment("Alice", "This is a comment.")
print(f"Автор: '{comment.author}'")
print(f"Текст: '{comment.text}'")

# Попытка присвоить пустые или состоящие только из пробелов строки
try:
    comment.author = ""  # Ожидается ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    comment.text = "   "  # Ожидается ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

# Попытка присвоить не строку
try:
    comment.author = 123  # Ожидается TypeError
except TypeError as e:
    print(f"Ошибка: {e}")

# Пример с пробелами
comment_with_space = Comment("  Bob  ", "  Another comment.  ")
print(f"Автор с пробелами: '{comment_with_space.author}'")  # Должны быть обрезаны
print(f"Текст с пробелами: '{comment_with_space.text}'")  # Должны быть обрезаны
