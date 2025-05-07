# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __iter__(self):
        n_str = str(self)
        for el in n_str:
            yield int(el)


n = IterInt(665)

for digit in n:
    print("digit = ", digit)
#

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6
