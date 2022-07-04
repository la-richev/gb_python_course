# Словарь — неупорядоченная последовательность, гибким к изменениям и индексированным. 
# В Python словари пишутся в фигурных скобках, и состоят из ключей и значений.

from colorama import Fore, Back, Style

print( Back.GREEN ) # добавляем цвет фона зеленый

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)

# Доступ к элементам
x = thisdict["model"]
print(x)

# изменяем элементы словаря
thisdict["year"] = 2018
print(thisdict)

# цикл for по словарю
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])
# or
for x in thisdict.values():
    print(x)

for x in thisdict.items():
    print(x)

# колличество элементнов (длина)
print(len(thisdict))

# add new element
thisdict["color"] = "red"
print(thisdict)

# Delete
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

# Ключевое слово del удаляет элемент по ключу
del thisdict["year"]
print(thisdict)

# Ключевое слово del может так же удалить полностью весь словарь

thisdict.clear()
print(thisdict)

# print("Год выпуска автомобиля: ", х)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['cycling', 'photo', 'singing'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}

print(person)
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

print(person['hobbies'][2]) # запись без переменных

print(person['children'])
children = person['children']
print(children['son'])
print(person['children']['son']) 

person['car'] = 'Mazda' # добавляем ключ/значение
person['hobbies'][0] = 'basketbal' # заменяем значение
print(person)

print (Back.BLACK)
# вывести только ключи
print(person.keys())
print(children.values()) # мы выше задали значения переменной children = person['children']

print (Back.RED)
# вывести только значения
print(person.values())

# вывести все элементы (выводится в виде кортежа)
print(person.items())

