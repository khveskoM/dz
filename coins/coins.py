#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:

    if (a >= b or b >= a) and b >= c:
        return a + b
    elif a >= c and c >= b:
        return a + c
    else:
        return b + c


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("a = "))
    c = int(input("a = "))

    print(max_sum_of_2(a, b, c))
