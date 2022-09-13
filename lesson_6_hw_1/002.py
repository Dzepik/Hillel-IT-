"""  функція, що знаходить різницю між максимальним та мінімальним значенням
   з num_limit випадкових чисел згенерованих
  в заданому діапазоні lower_bound..upper_bound.
"""
import random


def diff_min_max():
    lenght = int(input('Enter the list size: '))

    my_list = []
    for i in range(lenght):
        my_list.append(random.randint(1,100))

    print(f'Your random generated list of lenght {lenght} is:')
    print(my_list)

    result = max(my_list) - min(my_list)
    print(result)

diff_min_max()



def diff_min_max():
    lenght = int(input('Enter the list size: '))
    my_list = [random.randint(1, 200) for _ in range(lenght)]
    print(my_list)
    return max(my_list) - min(my_list)



print(diff_min_max())
