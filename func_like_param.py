def f():
    print('hello from other f')

def to(f_param):
    # параментром будет функция
    # поэтому в теле функции to мы ее вызовем
    f_param()

to(f)

# why
def my_filter(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_filter(numbers))

# если нужны нечетные числа
# если нужны числа > 4

# Можно использовать передачу парамента в виде функции
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number): # если функция вернет True, тогда мы будем записывать в результат это число, 
            #если False то записывать не будем
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# функ для четных
def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even))

# нечетн
def is_not_even(number):
    return number % 2 != 0

print(my_filter(numbers, is_not_even))

# числа > 4
def big_4(number):
    return number > 4

print(my_filter(numbers, big_4))

# Лямбда (запись в 1 строку, как параметр)
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number): # возвращает True значения
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# def is_even(number):
#     return number % 2 == 0
print(my_filter(numbers, lambda number: number % 2 == 0))

# def is_not_even(number):
#     return number % 2 != 0
print(my_filter(numbers, lambda number: number % 2 != 0))

# def big_4(number):
#     return number > 4
print(my_filter(numbers, lambda number: number > 4))
