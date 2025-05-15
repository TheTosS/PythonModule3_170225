# Проверить, начинается ли заданная строка с фразы "Начало:".
import re

string = "Начало: а дальше какой-то текст!"
pattern = re.compile(r"Начало:")

result = re.match(pattern, string)

if result:
    print("Строка начинается с ...")
else:
    print("Строка не начинается")