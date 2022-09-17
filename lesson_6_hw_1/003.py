"""
 функція, що знаходить різницю між сумою усіх парних чисел та сумою усіх непарних чисел
 серед num_limit випадкових чисел, згенерованих в заданому діапазоні
"""
import random



def diff_min_max():

    lenght = int(input('Enter the list size: '))

    my_list = []
    positive = 0
    negative = 0
    for i in range(lenght):
        my_list.append(random.randint(1,100))
    for i in my_list:
        if i % 2 == 0:
            positive += i
        elif i % 2 != 0:
            negative += i
    print(f'Your random generated list of lenght {lenght} is:')
    print(my_list)
    print('Sum of positive numbers =', positive)
    print('Sum of negative numbers =', negative)
    result = positive - negative
    print('The difference between the sum of paired and unpaired numbers =', result)


diff_min_max()





