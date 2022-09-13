"""
функція, що повертає найбільшу цифру випадково згенерованого
12-ти-значного натурального числа.
"""

from random import randint

def get_max_digit():
    number = randint(100000000000, 999999999999)
    print(number)
    r = -1
    while number > 10:
        d = number % 10
        number //= 10
        if d > r:
            r = d
    return r


print(get_max_digit())


def get_max_digit_2():
    number = randint(100000000000, 999999999999)
    print(number)
    s = str(number)
    ls = list(map(int, s))
    r = max(ls)
    return r


print(get_max_digit_2())







