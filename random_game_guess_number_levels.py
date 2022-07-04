# Развитие random_game_guess_number_count.py
# Добавляем уровни слодности и выбор урочня сложности

import random

number = random.randint(1, 100) # Созданием рандомное число
print(number)

# 1. Добавляем уровни сложности в виде словаря
levels = {'Easy': 10, 'Middle': 6, 'Hard': 3}
# 3. Вводим возможность вводить уровни сложности пользователю
level = input('Введите уровень сложУности (Easy, Middle, Hard): ')

user_number = None # Нужно чтобы мы прошли проверку while number != user_number и мы зашли в цикл
count = 0 # Кол-во попыток, = 0 пока мы не сделали не одной попытки
# 2. Добавляем max_count = levels['Easy'] для теста, а потом меняем на переменную level
max_count = levels[level]

# доработает цикл while
while number != user_number:
    count += 1 # будем увеличивать кол-во попыток +1, чтобы учитывать сколько раз пытался угадать число
    if count > max_count:
        print('GAME OVER') #чтобы не выподилась 'Вы угадали, это Победа!' мы добавили к while -> else
        break
    print(f'Попытка № {count}') # f новый способ форматирования строки https://shultais.education/blog/python-f-strings?
    #print('Попытка № {}'.format(count))
    #print('Попытка № {count}'.format(count=count))
    # Ввести число
    user_number = int(input('Введите число: '))
    # Сравнение чисел. Вывод промежуточного результата
    if user_number < number:
        print('Ваше число меньше загаданного')
    elif user_number > number:
        print('Ваше число больше загаданного')
else:
    print('Вы угадали, это Победа!')