# записать в список только положительные числа

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

# классический способ
result = []
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

# через функцию фильтер
result = filter(lambda number: number > 0, numbers) # на входе число number, на выходе number > 0
print(list(result))

# через герератор
result = [number for number in numbers if number > 0] # слева у нас переменная которую мы записываем в список, а справа условие
print(result)