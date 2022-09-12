#   Для введеного числа x виводить значення sign(x)


def sing(x):
    if x > 0:
        x = 1
    elif x < 0:
        x = -1
    else:
        x = 0
    return x


x = int(input('Введіть число: '))
print(sing(x))




