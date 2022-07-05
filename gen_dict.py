# Генерация словаря из кортежей

from unittest import result


pairs = [(1, 'Di'), (2, 'Kate'), (3, 'Yura')]
print(pairs)

# Классич способ
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)

# Через генератор словаря
result = {pair[0]: pair[1] for pair in pairs}
print(result)