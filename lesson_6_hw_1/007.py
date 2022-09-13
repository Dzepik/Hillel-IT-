"""
Угадай число!
"""

import random

number = random.randint(1,10)
user = -1
while user != number:
    print('Угадай число от 1 до 10')
    user = int(input('Введите число :'))
    if user > number:
        print('Число должно быть меньше!')
    elif user < number:
        print('Число должно быть больше!')
    else:
        print('Вы угадали это число')


