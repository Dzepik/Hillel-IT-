"""
 функція, що знаходить різницю між сумою усіх парних чисел та сумою усіх непарних чисел
 серед num_limit випадкових чисел, згенерованих в заданому діапазоні
"""
import random

num_limit = int(input('Enter the list size: '))
upper_bound = 0
lower_bound = 0

def diff_min_max(num_limit, lower_bound, upper_bound):

    my_list = []
    for i in range(num_limit):
        my_list.append(random.randint(1,100))
    for i in my_list:
        if i % 2 == 0:
            upper_bound += i
        elif i % 2 != 0:
            lower_bound += i
    print(f'Your random generated list of lenght {num_limit} is:')
    print(my_list)
    print('Sum of positive numbers =', upper_bound)
    print('Sum of negative numbers =', lower_bound)
    result = upper_bound - lower_bound
    return result
diff_min_max(10, 1, 100)









