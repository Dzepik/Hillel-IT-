"""
функція copydeep(lst), що створює глибоку копію довільного списку.
"""
#from copy import deepcopy

#lst1 = ['a', 1, 2.0, ['b']]
#lst2 = deepcopy(lst1)
#lst1[3].append(0)
#print(lst1[3], lst2[3])  # ['b', 0] ['b']

lst = ['a', 1, 2.0, ['b']]

def copydeep(lst):
    clone = lst.copy()
    return clone

print(copydeep(lst))

