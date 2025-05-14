# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную кириллическую букву
# 4) все слова начинающиеся на согласную кириллическую букву
# 5) все уникальные(без дубликатов) знаки препинания (знаками препинания считать символы .,!?;:)
import re

text = "quick brown fox jumps over there, near the lazy dog. THE end."

# 1
first_word_template = r"^\w+"
first_word = re.findall(first_word_template, text)
print(first_word)

# 2
...

# 5
signs_template = r"[.,!?;:]"
signs = re.findall(signs_template, text)
print(set(signs))