print("Игра УГАДАЙ ЧИСЛО")
number = 55
value = int(input("Угадай число от 1 до 100: "))

while value != number:
    print("Вы ввели число меньше. Попробуйте еще раз")
    value = int(input("Угадай число от 1 до 100: "))

print("Ура, Вы угадали!!!")

#if value < number:
#    print("Вы ввели число меньше. Попробуйте еще раз")
#elif value > number:
#    print("Вы ввели число больше. Попробуйте еще раз")
#else:
#    print("Вы угадали")

print("END GAME")