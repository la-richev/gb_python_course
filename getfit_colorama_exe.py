from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

print("------+^-+-^+------")
user_name = input(Fore.RED + "Как тебя зовут: ")
# print(Back.BLACK + 'Пользователь ввел:', user_name)
#print(type(user_name))
print(Style.RESET_ALL)

birth_year = int(input(Fore.RED + "Введите год вашего рождения: "))
year = int(input(Fore.RED + "Введите какой сейчас год: "))
print("Это високосный год:", year%4 == 0)

age = year - birth_year
print("Уважаемый", user_name, "вам сейчас:", age, "лет")
if age < 18:
    print("Доступ запрещен")
# иначе вывести на экран "Доступ разрешен"
elif age == 18:
    print("Вам ровно 18 лет, что же с вами делать?")
else:
    print("Доступ разрешен")
    if age % 5 == 0:
        print("Поздлавляем, у вас Юбилей в этом году был!")

#average life expectancy in Russia
ale = int(input("Введите предпологаемую продолжительность жизни: "))

dead = ale - age
print(Back.GREEN + "Вам осталось жить:", dead, "лет")
print(Back.GREEN + "Это всего:", dead*365, "дней")

# / - деление и // - целая часть от деления
live_part = age / ale
print(Back.RED + "Часть прожитой жизни:", round(live_part*100), "%")
#live_part = age // ale
#print("Часть прожитой жизни:", live_part)

dead_year = birth_year + ale
print(Back.RED + "Ваш примерный год смерти:", dead_year)

# print("У вас скоро юбилей:", (age+1) % 5 == 0) #age % 5 остаток от деления на 5
# print("У вас в этом году НЕ был юбилей:", age%5 != 0) # не равно !=
# print("У вас в этом году НЕ был юбилей:", not age%5 == 0) # not обратное выражение
# print("У вас юбилей И возраст меньше ALE:", age%5 == 0 and age < ale) # and
# print("У вас юбилей ИЛИ возраст меньше ALE:", age%5 == 0 or age < ale) # or
print(Style.RESET_ALL)
print("END")

input() #чтобы .exe сразу не закрывалась