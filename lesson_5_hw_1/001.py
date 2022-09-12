#   функцію, що визначає чи введене число є парним


def is_even(n):
    return n % 2 == 0


n = int(input("Введите число: "))
if is_even(n):
    print("Число четное!")
else:
    print("Число нечетное!")
