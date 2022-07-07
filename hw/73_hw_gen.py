# 3. Напишите функцию которая принимает на вход список. 
# Функция создает из этого списка новый список из квадратных корней чисел 
# (если число положительное) 
# и самих чисел (если число отрицательное) и возвращает результат 
# (желательно применить генератор и тернарный оператор при необходимости). 
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла. 
# Не забудьте включить туда отрицательные числа. 
# 10-20 чисел в списке вполне достаточно.

import math

old_list = [1, -3, 4, 35, 15, 12, 45, 13, 17, 25, 90, 4, 5, 10, 16, 100, 30, 50, 40, 37, -1, -2, -3, -10, -15, -40, -33]

# def sqrt(lst):
#     result = [math.sqrt(number) if number > 0 else number for number in lst]
#     return result

# print(sqrt(old_list))
# print(old_list)

def square(numlist):
    result = []
    for i in range(len(numlist)):
        number = numlist[i]**0.5 if numlist[i] > 0 else numlist[i]
        result.append(number)
        return result
print(square(old_list))


# def sqrt(lst):
#     result = [math.sqrt(number) if number > 0 else number for number in lst]
#     return result

# print(sqrt(old_list))
# print(old_list)