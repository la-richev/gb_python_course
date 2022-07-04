# Развитие random_game_guess_number_levels.py
# Добавляем игроков, ввод имен, поочередный ход, объявление победителей
print('ИГРА УГАДАЙ ЧИСЛО ОТ 1 ДО 100')
import random

number = random.randint(1, 100) # Созданием рандомное число
# print(number)

# Добавляем уровни сложности в виде словаря
levels = {'Easy': 10, 'Middle': 6, 'Hard': 3}
# Вводим возможность вводить уровни сложности пользователю
level = input('Введите уровень сложности (Easy, Middle, Hard): ')

user_number = None # Нужно чтобы мы прошли проверку while number != user_number и мы зашли в цикл
count = 0 # Кол-во попыток, = 0 пока мы не сделали не одной попытки
# Добавляем max_count = levels['Easy'] для теста, а потом меняем на переменную level
max_count = levels[level]

# 1. Добавим возможность добавления игроков
player_count = int(input('Введителе кол-во игроков: '))
players = [] # объявим список для сохранения имен игроков
for i in range(player_count):
    player_name = input(f'Введите имя игрока #{i+1}: ')
    players.append(player_name)

# 3. Чтобы определить победителя нало переработать логику наших циклов
is_winner = False # у нас пока нет победителя
winner_name = None # пустая строка, имя победителя

# 4. Меняем условия в цикле while
while not is_winner:
    count += 1 # будем увеличивать кол-во попыток +1, чтобы учитывать сколько раз пытался угадать число
    if count > max_count:
        print('GAME OVER') #чтобы не выподилась 'Вы угадали, это Победа!' мы добавили к while -> else
        break
    print(f'Попытка № {count}') # f новый способ форматирования строки https://shultais.education/blog/python-f-strings?
    #print('Попытка № {}'.format(count))
    #print('Попытка № {count}'.format(count=count))
# 2. Реализовать функционал для игроков. Мы их будем перебирать в цикле
    for player in players:
        print(f'Ход пользователя {player}')
        # Ввести число
        user_number = int(input('Введите число: '))
        print(f'Осталось попыток: {max_count-count+1}')
# 5. Добавляем условие
        if user_number == number:
            is_winner = True # у нас появился победитель
            winner_name = player # сохраняем его имя
            break
        # Сравнение чисел. Вывод промежуточного результата
        if user_number < number:
            print('Ваше число меньше загаданного')
            print('')
            print('--- Ходит другой игрок ---')
        elif user_number > number:
            print('Ваше число больше загаданного')
            print('')
            print('--- Ходит другой игрок --->')
else:
    print('Вы угадали, это Победа!')
    print(f'Победитель {winner_name}')