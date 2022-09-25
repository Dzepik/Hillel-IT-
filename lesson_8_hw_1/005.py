"""
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку.
"""

def gen_primes(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x==0:
            return False
    else:
        return True

result = list(filter(gen_primes, range(1,101)))
print(result)