# Задание "Упрощение дроби"
import re
import math


def parse_fraction(fraction: str)-> tuple:
    # "65/12"
    match = re.match(r"^(-?)(?:(\d+)\s)?(?:(\d+)/(\d+))?", fraction.strip())

    if not match:
        raise ValueError("Invalid fraction format")

    sign_str = match.group(1)
    whole_part = int(match.group(2)) if match.group(2) else 0
    numerator = int(match.group(3)) if match.group(3) else 0
    denominator = int(match.group(4)) if match.group(4) else 1

    return sign_str, whole_part, numerator, denominator


def simplificator(fraction: str) -> str:
    sign, whole_part, numerator, denominator = parse_fraction(fraction)
    print(f"{whole_part=}")
    print(f"{numerator=}")
    print(f"{denominator=}")

    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    whole_part += numerator // denominator
    numerator %= denominator

    return f"{sign}{whole_part} {numerator}/{denominator}"


# Простые дроби заданы в виде строки формата: целая_часть числитель/знаменатель
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# если целая часть присутствует, то всегда отделяется от дробной пробелом
# дроби могут быть отрицательными или положительными
# Примеры дробей
fraction1 = "3 12/15"
fraction2 = "-1 11/6"
fraction3 = "2/4"
fraction4 = "-5/4"

# TODO: Задание: Напишите функцию simplificator, которая возвращает дробь в упрощенном виде с выделением целой части
# print(simplificator("3 12/15"))  # --> 3 4/5
# print(simplificator("-1 11/6"))  # --> -2 5/6
# print(simplificator("2/4"))  # --> 1/2
# print(simplificator("-5/4"))  # --> -1 1/4
# print(simplificator("5"))  # --> 5
print(simplificator("-2/8"))  # --> -1/4
# Подсказки: смотри файл helpers/lcmp_gcd.py

# 13/7 -> 1 6/7
# 12/8 -> 3/2 -> 1 1/2
