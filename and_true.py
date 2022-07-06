# Создать список из чисел которые имеют кв корень меньше 2
import math
numbers = [1, 2, 3, 4, 5, -1, -2, -3, 16, 7, 10]

result = []
# обычный способ
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        # квадратный корень меньше 2
        if sqrt < 2:
            result.append(number)
print(result)

result = []
# через ленивый and
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# через генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)