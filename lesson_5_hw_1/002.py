#  функцію для рішення квадратних рівнянь

import math


print('Введите коэффициенты для уравнения')
print('ax^2 + bx + c = 0')
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x1 = -b / (2 * a)
        return x1, None
    else:
        return None, None


print(solve_quadratic_equation(a, b, c))


