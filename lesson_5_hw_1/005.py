#   Для введеного числа x виводить значення sign(x)


def sing(x):
    if x > 0:
        print('sing(x) = 1')
    elif x < 0:
        print('sign(-x) = -1')
    else:
        print('sign(x) = 0')


x = int(input('Введіть число: '))
sing(x)




