import requests

name = input('Введи своё имя: ')
age = input('Введи свой возраст: ')

while name != 'ник':
    print('нет')
    name = input('Введи своё имя: ')

if int(age) < 0:
    print('Ошибка,повторите ввод ')

elif int(age) <= 9:
    print('Привет, шкет')

elif int(age) <= 18:
    print(f'Как жизнь {name}')

elif int(age) < 101:
    print(f'Что желаете {name}')

else:
    print(f'{name},вы лжете в наше время столько не живут... ')