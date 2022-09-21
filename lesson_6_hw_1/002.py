"""  функція, що знаходить різницю між максимальним та мінімальним значенням
   з num_limit випадкових чисел згенерованих
  в заданому діапазоні lower_bound..upper_bound.
"""
import random


def diff_min_max():
    lenght = int(input('Enter the list size: '))

    num_limit = []
    for i in range(lenght):
        num_limit.append(random.randint(1,100))

    print(f'Your random generated list of lenght {lenght} is:')
    print(num_limit)

    result = max(num_limit) - min(num_limit)
    print(result)

diff_min_max()



def diff_min_max():
    lenght = int(input('Enter the list size: '))
    num_limit = [random.randint(1, 200) for _ in range(lenght)]
    print(num_limit)
    return max(num_limit) - min(num_limit)



print(diff_min_max())
