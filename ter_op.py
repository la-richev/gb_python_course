# Тернарный оператор

is_has_name = True
name = 'Max' if is_has_name else 'Empty'
print(name)

is_has_name = False
name = 'Max' if is_has_name else 'Empty'
print(name)

is_has_name = False
name = '1' if is_has_name else '2'
print(name)

is_russian = False
print('Привет' if is_russian else 'Hello')

is_russian = True
print('Привет' if is_russian else 'Hello')