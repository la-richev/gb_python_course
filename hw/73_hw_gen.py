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

# 1
result = []
for i in old_list:
    if i > 0:
        number = math.sqrt(i)
        result.append(number)
    else:
        result.append(i)
print(result)
print(old_list)

# 2
print('Решение с помощью функции:')

def sqrt_easy(list):
    result = []
    for i in list:
        if i > 0:
            number = math.sqrt(i)
            result.append(number)
        else:
            result.append(i)
    return result

print(sqrt_easy(old_list))
print(old_list)

# 3 
print('Решение с помощью функции и тернарного опаратора:')
def sqrt_easy_ter(list):
    result = []
    for i in list:
        number = math.sqrt(i) if i > 0 else i
        result.append(number)
    return result

print(sqrt_easy_ter(old_list))
print(old_list)

# 4
print('Решение с помощью функции, генератора и тернарного опаратора:')

def sqrt(list):
    result = [math.sqrt(number) if number > 0 else number for number in list]
    return result

print(sqrt(old_list))
print(old_list)