# 4. Написать функцию которая принимает на вход число от 1 до 100. 
# Если число равно 13, функция поднимает исключительную ситуации ValueError 
# иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число. 
# Введенное число передаем параметром в написанную функцию и печатаем результат, 
# который вернула функция. 
# Обработать возможность возникновения исключительной ситуации, 
# которая поднимается внутри функции.

import math
from unittest import result

# Без функции
number = int(input('Без функции, квадратный корень числа // Введите число от 1 до 100: '))

if number > 0 and number < 100 and number != 13:
    number = math.sqrt(number)
    print(number)
else:
    try:
        raise ValueError
    except:
        print('Не вводите 13, введите другое число от 1 до 100')

# Def
def square(n):
    if n > 0 and n < 100 and n != 13:
        n = (n ** 2)
        return n
    else:
        try:
            raise ValueError
        except:
            print('Не вводите 13, введите другое число от 1 до 100')

number = int(input('Функция, квадрат числа // Введите число от 1 до 100: '))
print(square(number))

# Интересное решение пользователей:
# def square(number):
#     if number == 13 or number < 0 or number > 100:
#         try:
#             raise ValueError
#         except:
#             print('Введено число вне диапазона [1, 12], [14, 100]')
#     else:
#         result = [number ** 2]
#         return result

# n = int(input('Введите число от 1 до 100, кроме 13: '))
# print(square(n))

# решение преподавателя
print('Решение преподавателя:')
def unlucky_number(number):
    if number == 13:
        raise ValueError("It's unlucky number!")
    else:
        return number ** 2

number = int(input('Функция, квадрат числа // Введите число от 1 до 100: '))

try:
    result = unlucky_number(number)
except ValueError:
    print('У нас несчастливое число')
else:
    print(result)
    