# Алгоритм по нахождению второго по величине максимального числа
# Первый способ (самый простой, но плохо плохая реализация)

numbers = [1, 8, 3, 2, 6]
size = len(numbers) # 5
print(size)
current_index = 0
max = numbers[0]
max_current_index = 0 # на текущий момент я считаю этот элемент является самым большим ПЕРВЫМ

print(f'Веса гирь: {numbers}, Кол-во гирь: {size}, // {current_index}, {max}, {max_current_index}')

while current_index < size:
    if numbers[current_index] > max:
        max = numbers[current_index]
        max_current_index = current_index
    current_index = current_index + 1
print('Самое большое число в последовательности: ', max)
print('# самого большим ПЕРВЫМ: ', max_current_index)

current_index = 0
second_max = numbers[0]
second_max_index = 0 # на текущий момент я считаю этот элемент является самым большим ВТОРЫМ

# if max_current_index == 0:
#     second_max = numbers[1]

while current_index < size:
    if numbers[current_index] != max_current_index:
        if numbers[current_index] > second_max_index:
            second_max = numbers[current_index]
            second_max_index = current_index

    current_index = current_index + 1

print('Самое большое ВТОРОЕ число в последовательности: ', second_max)
print('# самого большого ВТОРОГО: ', second_max_index)