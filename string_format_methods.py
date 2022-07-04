name = 'Dima'
print(name.upper())
print(name.lower())
print(name) # строки неизменные, методы lower and upper создают новую строку

long_string = 'This is the long string'
print(long_string.split()) # строка разбивается ввиде листа
print(long_string.split('s')) # разделитель буква s

name = 'Dima'
age = 37
role = 'trainer'

name_and_age = 'My name is {0}, I\'m {1} and {2}'.format('Dima', 37, 'trainer')
print(name_and_age)

name_and_age = 'My name is {0}, I\'m {1} and {2}'.format(name, age, role)
print(name_and_age)

name_and_age = 'My name is {}, I\'m {} and {}'.format(name, age, role)
print(name_and_age)

# появилось только в Python 3.6+
name_and_age = f'My name is {name}, I\'m {age} and {role}'
print(name_and_age)

date = 'This week is: {mo}, {tu}, {we}, and more'.format( mo = 'Monday', tu = 'Tuesday', we = 'Wednesday')
print(date)

float_result = 1000/7
print(float_result)
print('The result of devision is {0:10.3f}'.format(float_result))

# Старый способ записи в py2 (не рекомендуется использовать уже)
name = 'Dima'
age = 37
name_and_age = 'My name is %s, I\'m %d and %s' % (name, 37, 'trainer')
print(name_and_age)