# Создать список из случайных чисел от 1 до 100
import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# Создать список квадратов числе
numbers = [1, 2, 3, -4]

numbers = [number**2 for number in numbers]
print(numbers)

# Создать список имен на букву А
names = ['Руслан', 'Dmitry', 'Andrey', 'Alex', 'Алан']

names = [name for name in names if name.startswith('A')]
print(names)