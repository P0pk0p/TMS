import requests
import random

guesses_made = 0

name = input('Введите что-нибудь')
number = random.randint(1, 10)
print(' Число загадоно между 1 и 10.')
while guesses_made < 3:
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess < number:
        print('Твое число меньше загаданного.')

    if guess > number:
        print('Твое число больше загаданного .')

    if guess == number:
        break

if guess == number:
    print('Ты угадал число, использовав {1} попыток!'.format(guesses_made))
else:
    print('А вот и не угадал! Загаданного число {0}'.format(number))