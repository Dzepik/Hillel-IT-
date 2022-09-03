import math


def triangle_square_and_perimeter(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    S = (a * b) / 2
    P = a + b + c
    return(S, P)
a = int(input('Введите значение первого катета: '))
b = int(input('Введите значение второго катета: '))
z = triangle_square_and_perimeter(a, b)
print(z)
