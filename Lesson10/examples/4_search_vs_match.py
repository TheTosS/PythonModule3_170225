import re

text = "футбол баскетбол волейбол"
pattern = r"баскетбол"

# Используем re.search()
search_match = re.search(pattern, text)
if search_match:
    print(f"re.search() нашел: '{search_match.group()}' по индексам {search_match.span()}")
else:
    print("re.search() ничего не нашел")

# Используем re.match()
match_match = re.match(pattern, text)
if match_match:
    print(f"re.match() нашел: '{match_match.group()}' по индексам {match_match.span()}")
else:
    print("re.match() ничего не нашел")

print("-" * 20)

text2 = "баскетбол волейбол футбол"  # Шаблон теперь в начале
pattern = r"баскетбол"

# Используем re.search()
search_match2 = re.search(pattern, text2)
if search_match2:
    print(f"re.search() нашел: '{search_match2.group()}' по индексам {search_match2.span()}")

# Используем re.match()
match_match2 = re.match(pattern, text2)
if match_match2:
    print(f"re.match() нашел: '{match_match2.group()}' по индексам {match_match2.span()}")
