class IterInt(int):
    def __iter__(self):
        n_str = str(self)
        for el in n_str:
            yield int(el)

n = IterInt(12534)
max_digit = max(n)
print(max_digit)
# Найти наибольшую цифру в числе, используя итерацию по цифрам IterInt.