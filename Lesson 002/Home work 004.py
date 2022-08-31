from decimal import Decimal

b = Decimal(input('Введіть кількість гривень:' ))
a = Decimal('40.7')
x = round(b / a, 1)
print('Станом на 27 серпня 2022 року це становить' , x, 'Долари США')
