"""
функція index(lst, elem), що повертатиме індекс elem в списку lst, або,
якщо елемент відсутній, то None.
"""

lst = [1, 3, 7, 11, 67, 444]
elem = 768

def index(lst, elem):
    for i, k in enumerate(lst):
        if k == elem:
            return i
    return None

print(index(lst, elem))




