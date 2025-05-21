# Задание "Простые дроби"
import re
import math

# 2 1/2 -> 5/2
# -3 3/7 -> -24/7 -> 3 3/7


class Fraction:
    def __init__(self, raw_fraction):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        sign, whole, numerator, denominator = self.simplificator(raw_fraction)
        self.numerator = whole * denominator + numerator  # числителя
        self.denominator = denominator  # знаменателя
        if sign == "-":
            self.numerator *= -1

    @staticmethod
    def parse_fraction(fraction: str) -> tuple:
        match = re.match(r"^(-?)(\d*)(?:\s*(\d+)/(\d+))?$", fraction.strip())

        if not match:
            raise ValueError("Invalid fraction format")

        sign_str = match.group(1)
        whole_part = int(match.group(2)) if match.group(2) else 0
        numerator = int(match.group(3)) if match.group(3) else 0
        denominator = int(match.group(4)) if match.group(4) else 1

        return sign_str, whole_part, numerator, denominator

    @staticmethod
    def simplificator(fraction: str) -> tuple:
        sign, whole_part, numerator, denominator = Fraction.parse_fraction(fraction)

        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd

        whole_part += numerator // denominator
        numerator %= denominator

        return sign, whole_part, numerator, denominator

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        whole = self.numerator // self.denominator
        numerator = self.numerator % self.denominator
        return f"{whole} {numerator}/{self.denominator}"


# Простые дроби заданы в виде строки

# Конструктор принимает простую дробь в виде строки формата: <Целая часть> <числитель>/<знаменатель>
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# дроби могут быть отрицательными или положительными
f1 = Fraction("3 12/15")
f2 = Fraction("-1 11/6")
f3 = Fraction("2/4")
f4 = Fraction("-5/4")

# TODO: Задание: реализуйте class Fraction, который выводит дробь в упрощенном виде с выделением целой части
print(f1)  # 3 4/5
print(f2)  # -2 5/6
print(f3)  # 1/2
print(f4)  # -1 1/4
