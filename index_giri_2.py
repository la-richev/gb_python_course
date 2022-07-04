# Алгоритм по нахождению второго по величине максимального числа

numbers = [2, 8, 3, 3, 6]
size = 5
first = numbers[0]
second = numbers[0]

if numbers[1] > first:
    first = numbers[1]
else:
    second = numbers[1]

print(first)
print(second)


