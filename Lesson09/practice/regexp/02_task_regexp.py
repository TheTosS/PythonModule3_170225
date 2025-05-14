# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найти все слова "the" в тексте, игнорируя регистр и убедившись,
# что это именно слово, а не часть другого слова (например, "there").
import re

text_modified = "The quick brown fox jumps over there, near the lazy dog. THE end."
template = r"\bthe\b"
result = re.findall(template, text_modified.lower())

print(result)
