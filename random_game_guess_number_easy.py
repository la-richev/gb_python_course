# Развитие random_number.py
# Создание рандомного числа

import random

number = random.randint(1, 100)
print(number)

while True:
    # Ввести число
    user_number = int(input('Введите число: '))
    # Сравнение чисел
    if user_number == number:
        print('Вы угадали, это Победа!')
        break
    elif user_number < number:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')

