import re

# Компиляция шаблона один раз
pattern_string = r'\d+'
compiled_regex = re.compile(pattern_string)

# Теперь используем скомпилированный объект для выполнения операций
text1 = "У меня есть 3 яблока и 5 груш."
text2 = "Мне нужно 10 минут."

# Вместо re.search(pattern_string, text1) используем compiled_regex.search(text1)
match1 = compiled_regex.search(text1)
if match1:
    print(f"Найдено в тексте 1: {match1.group()}") # Вывод: Найдено в тексте 1: 3

# Вместо re.findall(pattern_string, text2) используем compiled_regex.findall(text2)
matches2 = compiled_regex.findall(text2)
print(f"Все числа в тексте 2: {matches2}") # Вывод: Все числа в тексте 2: ['10']