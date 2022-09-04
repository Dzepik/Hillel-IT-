#  функцію для рішення квадратних рівнянь


a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('Дискриминант = 0')
        print('Решений нет')
    elif D == 0:
        x = (-b + D ** .5) / (2 * a)
        print('Дискриминант =', D)
        print('Корень один: ', x)
    else:
        x_1 = (-b + D ** .5) / (2 * a)
        x_2 = (-b - D ** .5) / (2 * a)
        print('Дискриминант =', D)
        print('Есть два корня: ')
        print('Корень 1 =  ', x_1)
        print('Корень 2 =  ', x_2)


solve_quadratic_equation(a, b, c)


