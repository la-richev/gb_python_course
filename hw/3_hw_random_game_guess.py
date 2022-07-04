import random

min_number = 1
max_number = 100

# Шаг 1
'''
while True:
    number = random.randint(min_number, max_number)
    print(number)
    result = input(' < = > ')
    if result == '=':
        print('Подеда')
        break
    elif result == '>':
        min_number = number + 1 # +1 чтобы то же самое число снова не угадывать
    elif result == '<':
        max_number = number - 1
'''

# Шаг 2 Улучшить: убрать бесконечный цикл while True
result = None # Чтобы войти в цикл надо объявить переменную result и присвоить ей значение, тк мы пока не знаем чему = результат

while result != '=': # 1) Цикл будет выполняться, пока результат не будет "не равен" =
    number = random.randint(min_number, max_number)
    print(number)
    result = input(' < = > ')
    if result == '>':
        min_number = number + 1 # +1 чтобы то же самое число снова не угадывать
    elif result == '<':
        max_number = number - 1

print('Подеда')