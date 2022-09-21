"""
функція, що розраховує суму Unicode кодів усіх символів,
що знаходяться між двома заданими символами включно.
"""

def sum_symbol_codes(first, last):
    my_list = list(map(ord, 'abcdefghijklmnopqrstuvwxyz'))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    go = alphabet.index(first)
    to = alphabet.index(last)

    return sum(my_list[go:to + 1])

print(sum_symbol_codes('a', 'm'))







