# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

# 1
name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите город: ')

def print_str():
    print(f'{name}, {age} год(а), проживает в городе {city}')

print_str()

# решение преподавателя
def person_info(name, age, city):
    result = f'{name}, {age} год(а), проживает в городе {city}'
    return result

print(person_info(name, age, city))


# 2
# numbers = []
# for i in range(3):
#     number = int(input('Введите число: '))
#     numbers.append(number)
# print(numbers)
# print(max(numbers))

numbers = []

def max_number(numbers):
    i = int(input('Input count: ')) # добавил еще переменную кол-ва чисел
    for i in range(i):
        number = int(input('Введите число: '))
        numbers.append(number)
    print(numbers)
    print(max(numbers))

max_number(numbers)

# решение преподавателя
def get_max(a, b, c):
    result = max([a, b, c])
    return result

result = get_max(1, 5, 3)
print(result)

# еще решение
numbers = []

def max_get(numbers):
    result = max(numbers)
    return result

i = int(input('Input count: ')) # переменная задает кол-во чисел в списке
for i in range(i):
    num = i + 1
    number = int(input(f'Введите число #{num}: '))
    numbers.append(number)

result = max_get(numbers)
print(result)