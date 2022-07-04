# 3: Давайте опишем пару сущностей player и enemy через словарь, 
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
### Поэкспериментируйте с значениями урона и жизней по желанию. 
# ### Теперь надо создать функцию attack(person1, person2). 
# Примечание: имена аргументов можете указать свои. 
### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
# Функция должна сама работать со словарями и изменять их значения.


player_name = input('Enter name of player 1: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50
}
print(player)

enemy_name = input('Enter name of player 2: ')
enemy = {
    'name': enemy_name,
    'health': 75,
    'damage': 75
}
print(enemy)

# выбор кто enemy (порядок хода)
# damages = health - damage

def attack(attacker, defender):
    defender['health'] = defender['health'] - attacker['damage']
    print(f'Игрок "{attacker["name"]}" [{attacker["health"]}] нанёс {attacker["damage"]} урона игроку "{defender["name"]}" [{defender["health"]}]')
    
attack(player, enemy)

# Решение преподавателя
print('Решение преподавателя')
player_name = input('Enter name of player 1: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50
}
print(player)

enemy_name = input('Enter name of player 2: ')
enemy = {
    'name': enemy_name,
    'health': 75,
    'damage': 75
}
print(enemy)

def attack_v2(attacker, defender):
    defender['health'] -= attacker['damage']

attack_v2(player, enemy)
print(enemy['health'])

attack_v2(enemy, player)
print(player['health'])

'''
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.
Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 
'''

player_name = input('Enter name of player 1: ')
player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.1}
print(player)

enemy_name = input('Enter name of player 2: ')
enemy = {'name': enemy_name, 'health': 75, 'damage': 75, 'armor': 1.2}
print(enemy)

def attack(attacker, defender):
    damage_armor = round(attacker['damage'] / defender['armor'])
    defender['health'] = defender['health'] - damage_armor
    print(f'Игрок "{attacker["name"]}" [{attacker["health"]}] нанёс {damage_armor} урона игроку "{defender["name"]}" [{defender["health"]}]')

attack(player, enemy)


# Решение преподавателя
print('Решение преподавателя_hard')

player_name = input('Enter name of player 1: ')
player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}
print(player)

enemy_name = input('Enter name of player 2: ')
enemy = {'name': enemy_name, 'health': 50, 'damage': 30, 'armor': 1}
print(enemy)

def split_damage(damage, armor):
    return damage / armor

def attack_3(attacker, defender):
    damage = split_damage(attacker['damage'], defender['armor'])
    defender['health'] -= damage

attack_3(player, enemy)
print(enemy['health'])

attack_3(enemy, player)
print(player['health'])