print("------+^-+-^+------")
user_name = input("Как тебя зовут: ")
print('Пользователь ввел:', user_name)
#print(type(user_name))

birth_year = int(input("Введите год вашего рождения: "))
year = int(input("Введите какой сейчас год: "))
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
print("Вам осталось жить:", dead, "лет")
print("Это всего:", dead*365, "дней")

# / - деление и // - целая часть от деления
live_part = age / ale
print("Часть прожитой жизни:", live_part*100, "%")
#live_part = age // ale
#print("Часть прожитой жизни:", live_part)

dead_year = birth_year + ale
print("Ваш примерный год смерти:", dead_year)

print("У вас скоро юбилей:", (age+1) % 5 == 0) #age % 5 остаток от деления на 5
print("У вас в этом году НЕ был юбилей:", age%5 != 0) # не равно !=
print("У вас в этом году НЕ был юбилей:", not age%5 == 0) # not обратное выражение
print("У вас юбилей И возраст меньше ALE:", age%5 == 0 and age < ale) # and
print("У вас юбилей ИЛИ возраст меньше ALE:", age%5 == 0 or age < ale) # or

print("END")