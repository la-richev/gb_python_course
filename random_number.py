# 1.Создание рандомного числа
import random

number = random.randint(1, 100)
print(number)

# 2.Ввести число
user_number = int(input('Введите число: '))
print(user_number)

# 3.Сравнение чисел
if user_number == number:
    print('Вы угадали, это Победа!')
elif user_number < number:
    print('Ваше число меньше загаданного')
else:
    print('Ваше число больше загаданного')

