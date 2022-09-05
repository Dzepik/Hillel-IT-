#   рекурсивна функцію, що приймає натуральне число і повертає число
#   з послідовності Фібоначі, позиція якого відповідає введеному числу



n = int(input('Введіть число: '))

def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    n_1 = fibonacci(n-1)
    n_2 = fibonacci(n-2)
    n = n_1 + n_2
    return n

print(fibonacci(n))