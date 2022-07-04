# 1. print, type, lenm input, float, str
# 2. abc, min, max, round, sum, enumerate

# 1.
# Печать - функ с параментрами
print('Hello')

# Функция может быть без параментров, но возвращать результат
name = input('Введите что-н: ')
print(name)

# Тип переменной - функ с парам и возвращ значением
t = type(123)
print(t)

# Диапазон - функ с парам и возвращ значением
r = range(10)
print(r)

# Длина последовательности
l = len([1, 2, 3, 10])
print(l)

# Преобразование типов
int('10')
str(10)

# 2.
# Модуль числа
print(abs(-7))

# min, max
numbers = [1, -2, 3, 10]
print(max(numbers))
print(min(numbers))

# round
print(round(10.94458767, 2))

# sum
print(sum(numbers))

# enumerate
winners = ['Leo', 'Kate', 'Di']
for number, winner in enumerate(winners, 1):
    print(number, winner)

# Example 
# Ввести 3 числа. Найти мах, сумму и вывести результа на экран

numbers = []

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))



