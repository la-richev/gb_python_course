# 2: Дан список, заполненный произвольными числами. 
# Получить список из элементов исходного, удовлетворяющих следующим условиям: 
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
# Примечание: Список с целыми числами создайте вручную в начале файла. 
# Не забудьте включить туда отрицательные числа. 
# 10-20 чисел в списке вполне достаточно.

numbers = [1, 2, 3, 7, 35, 15, 12, 45, 13, 17, 25, 90, 4, 5, 10, 16, 100, 30, 50, 40, 37, -1, -2, -3, -10, -15, -40, -33]

result = []
for number in numbers:
    if number > 0 and number % 3 == 0 and number % 4 != 0:
        result.append(number)

print(result)

result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]
print(result)