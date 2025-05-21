# Задание "Простые дроби"
import re
import math


class Fraction:
    def __init__(self, raw_fraction):  # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        sign, whole, numerator, denominator = self.simplificator(raw_fraction)
        print(f"{sign=}")
        print(f"{whole=}")
        print(f"{numerator=}")
        print(f"{denominator=}")
        self.numerator = whole * denominator + numerator  # числителя
        self.denominator = denominator  # знаменателя
        if sign == "-":
            self.numerator *= -1

    @staticmethod
    def parse_fraction(fraction: str) -> tuple:
        match = re.match(r"^(-?)(?:(\d+)\s)?(?:(\d+)/(\d+))?", fraction.strip())

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

    def __add__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        print(f"{new_numerator=}")
        print(f"{new_denominator=}")
        return Fraction(f"{new_numerator}/{new_denominator}")

    def __str__(self):
        """
        Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
        Пример: "-3 5/7"
        """
        print(f"{self.numerator}")
        print(f"{self.denominator}")
        whole = abs(self.numerator) // abs(self.denominator)
        numerator = abs(self.numerator) % abs(self.denominator)
        if self.numerator < 0:
            return f"-{whole} {numerator}/{self.denominator}"
        return f"{whole} {numerator}/{self.denominator}"


f1 = Fraction("1/2")
f2 = Fraction("-3/4")
# f3 = Fraction("2/4")
# f4 = Fraction("-3/4")
# TODO: Задание: реализуйте операции с дробями
# Сложение
f_sum = f1 + f2 # f1.__add__(f2)
# 4/8 -6/8
print(f"{f1} + {f2} = {f_sum}") # 2/4 + (-3/4) = -1/4
# # Вычитание
# f_sub = f3 - f4
# print(f"{f3} + {f4} = {f_sub}")
# # Умножение
# f_mult = f3 * f4
# print(f"{f3} * {f4} = {f_mult}")

