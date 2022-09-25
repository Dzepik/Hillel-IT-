"""
Створити генератор паролів, що генерує паролі сумісні з наступними вимогами:
1) Пароль складається з 8 символів
2) В паролі допускаються лише великі та маленькі латинські літери,
цифри та символ підкреслення "_"
3) Пароль обов'язково має містити щонайменше одну велику літеру,
одну маленьку літеру та одну цифру.
4) Не повинно бути більше 2 однакових символів підряд.
"""

from random import choice

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '_'
ally = digits + uppercase + lowercase + punctuation

chars = ''

pwd_pass = ['pwd_auto', 'pwd_digits', 'pwd_uppercase', 'pwd_lowercase', 'pwd_punctuation']
pwd_length = int(input('Введите желаемую длину пароля: '))
pwd_auto = input('Сгенерировать пароль автоматически? (y, n): ')
pwd_digits = input('Включить цифры (y, n): ')
pwd_uppercase = input('Включить uppercase (y, n): ')
pwd_lowercase = input('Включить маленькие буквы (y, n): ')
pwd_punctuation = input('Включить спец. символы (y, n): ')

for i in pwd_pass:
    if pwd_auto == 'y':
        chars += ally
    break
else:
    if pwd_digits == 'y':
        chars += digits
    if pwd_uppercase == 'y':
        chars += uppercase
    if pwd_lowercase == 'y':
        chars += lowercase
    if pwd_punctuation == 'y':
        chars += punctuation

password = ''

for i in range(pwd_length):
    password += choice(chars)

print('\n', password, '\n', sep='')