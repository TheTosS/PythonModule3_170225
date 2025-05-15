# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
import re


def parse_fraction(fraction: str):
    if fraction.isdigit():
        return '', fraction, None, None
    fraction_pattern = r"(-?)(?:(\d+)\s+)?(\d+)/(\d+)"
    match = re.match(fraction_pattern, fraction)
    if match:
        return match.groups()
    return None


def parse_expression(expression: str) -> tuple | None:
    sign_pattern = r"(.+)\s+([-+])\s+(.+)"
    match = re.match(sign_pattern, expression)
    if match:
        return match.groups()
    return None


if __name__ == "__main__":
    # tests parse_expression
    assert parse_expression("5/6 + 4/7") == ("5/6", "+", "4/7")
    assert parse_expression("-12 5/6 - 4/7") == ("-12 5/6", "-", "4/7")
    assert parse_expression("12 5/7 + 4 5/17") == ("12 5/7", "+", "4 5/17")
    # assert parse_expression("7 3/17 + -5/17") == ("7 3/17", "-5/17")
    # assert parse_expression("-5/7 - -2 5/12") == ("-5/7", "-2 5/12")
    # assert parse_expression("1/2 - 1/2") == ("1/2", "1/2")
    # TODO-3: доработайте функцию parse_expression, чтобы она возвращала ответ в формате
    #  ("первая дробь", "знак операции", "вторая дробь")
    # TODO-4: исправьте тесты, в соответствии с новой логикой работы функции

    # tests parse_fraction
    assert parse_fraction("-12 5/6") == ("-", "12", "5", "6")
    assert parse_fraction("5/6") == ("", None, "5", "6")
    assert parse_fraction("-7/12") == ("-", None, "7", "12")
    assert parse_fraction("4") == ("", "4", None, None)
    # assert parse_fraction("-15") == ("-", "15", None, None)
    # print(parse_fraction("4"))
    # TODO-1: допишите тесты для функции parse_fraction, чтобы выявить недостатки работы.
    # TODO-2: Исправьте функцию.


text = """
first string
second string
end!
"""