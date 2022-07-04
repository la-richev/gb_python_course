from random import randint, choice, sample, shuffle
import math

# 1. Загадать случ число от 0 до 100
print(randint(0, 100))
# 2. выбрать победителя из списка players
players = ['Max', 'Leo', 'Di', 'John']
print(choice(players))
# 3. выбрать 3х победителей из списка players
print(sample(players, 3))
# 4. перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)

# найти длину окружности с опред радиусом
r = 100
print(2*r*math.pi)
# найти площадь окружности с опред радиусом
print((r**2)*math.pi)
print((math.pow(r, 2))*math.pi)
# по координатам 2-х точек опред расстояние между ними
x1=10
y1=10
x2=50
y2=100
i = math.sqrt((x1-x2)**2+(y1-y2)**2) # решается по теореме пифагора
print(i)
# найти факториал числа 9
print(math.factorial(9))