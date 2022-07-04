# filter - фильтрация последовательности
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# получить только четные числа
def is_even(number):
    return number % 2 == 0

# вызываем функ фильтр
result = filter(is_even, numbers)
print(result)
result = list(result) # нужно привести к списку
print(result)

# Набор строк
names = ['Max', 'Alex', 'Kate']

# получить строки больше 3-х символов
print(list(filter(lambda x: len(x)>3, names)))

# map - не фильтр последовательность, а получает новую 
# map применяется в каждому элементу

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# получить список квадратов чисел 
print(list(map(lambda x: x**2, numbers)))

# привести числа к строке
print(list(map(lambda x: str(x), numbers))) 