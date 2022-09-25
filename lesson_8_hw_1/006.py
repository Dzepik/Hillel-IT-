"""
Напишіть функцію, яка прийматиме рядок та перетворюватиме його способом,
описаним вище.
"""

from random import shuffle
from copy import copy


def check_word(middle):
    for a in middle[1:]:
        if a != middle[0]:
            return True
    return False


def pemrtuate(text):
    lst = text.split(' ')
    new_string = ""
    for word in lst:
        l = len(word)
        middle = list(word[1:l - 1])
        if check_word(middle):
            sv = copy(middle)
            while True:
                shuffle(middle)
                if sv != middle:
                    break
            new_string += word[0] + ''.join(middle) + word[l - 1] + ' '
        else:
            new_string += word + ' '
    return new_string


print(pemrtuate("привет как дела новый телефон"))
