birthday_year = '1985' #строковый, тк в ''/""
print(type(birthday_year))

period = 20
print(type(period))

print(birthday_year, period) #через запятую можно вывести любые типы данных

age = period + int(birthday_year)
print(age)

some_str = str(period) + birthday_year
print(some_str)

my_name = 'Dima'
print(type(my_name))
print(my_name.upper()) # не роббит

#Форматирование строк
year = 30

#конкатенация
hello = "Привет " + my_name + " ты " + str(birthday_year) + " года рождения"
print(hello)

#%
hello = 'Привет %s тебе %d лет'%(my_name, year)
print(hello)

#format
hello = 'Привет {} тебе {} лет'.format(my_name, year)
print(hello)

top5 = "Первый пять мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров. 4. Орлов 5. Соколов"
# Поздравляем 1. 2. 3.
start = top5.find("1")
end = top5.find("4")

top3 = top5[start: end] # : -тк "срезы должны быть целые", что это?
result = "Поздравляем {}".format(top3.upper())
print(result)

