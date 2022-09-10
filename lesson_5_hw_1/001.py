#   функцію, що визначає чи введене число є парним


def check(n):
    return n % 2 == 0


n = int(input("Введите число: "))
if (check(n) == True):
    print("Число четное!")
else:
    print("Число нечетное!")
