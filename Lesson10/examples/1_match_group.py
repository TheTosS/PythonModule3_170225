import re

text = "Анна 30 лет"
pattern = r"(\w+)\s+(\d+)"  # Первая группа (\w+) - имя, вторая группа (\d+) - возраст

match = re.match(pattern, text)
if match:
    print(f"Все совпадение (group(0)): '{match.group(0)}'")     # Выведет 'Анна 30'
    print(f"Группа 1 (имя): '{match.group(1)}'")                # Выведет 'Анна'
    print(f"Группа 2 (возраст): '{match.group(2)}'")            # Выведет '30'
    print(f"Все группы (groups()): {match.groups()}")           # Выведет ('Анна', '30')
else:
    print("Совпадений не найдено.")
