# AND и OR ленивые операторы
# Как работает оператор AND - возвращается первое ЛОЖНОЕ условие
import math

if 1 > 2 and math.sqrt(-1): # Квадратный конень из -1 (но его извлечь нельзя!) поэтому будет ошибка
    print("Ошибки не будет тк первое условие ложь")
print('Next')

# Первая ложь
print([1] and [] and '' and 1)

# Последняя истина: если все истино, то возвращаться будет последнее истинное значение
print([1] and 1 and 20 and 1.1)

# Как работает оператор OR - возвращается первое ИСТИННОЕ условие
if 2 > 1 or math.sqrt(-1): # Квадратный конень из -1 (но его извлечь нельзя!) поэтому будет ошибка
    print("Ошибки не будет тк первое условие истина")
print('Next')

# Первая истина
print(0 or [] or 8 or 5)

# Последняя ложь: если все ложно, то возвращаться будет 1 ложное значение
print(0 or [] or () or {})