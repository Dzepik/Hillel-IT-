"""
функція, що розраховує суму Unicode кодів усіх символів,
що знаходяться між двома заданими символами включно.
"""

#def sum_symbol_codes():
    #a = ord('a')
    #b = ord('b')
    #c = ord('c')
    #d = ord('d')
    #result = a + b + c + d


    #return result

#print(sum_symbol_codes())



def sum_symbol_codes():
    my_list = list(map(ord, 'abcdefghijklmnopqrstuvwxyz'))
    first = ord('a')
    last = ord('d')
    while first < last:
        first = first + 1
    #result = my_list[0] + my_list[1] + my_list[2] + my_list[3]
    return first




print(sum_symbol_codes())




