#   визначити, чи є рік із введеним числом високосним.
#   Якщо рік є високосним, то виведеться `YES`, інакше виведеться `NO`.


year = int(input('Введіть число: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')