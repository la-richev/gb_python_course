# List (список) — упорядоченная последовательность, которую можно изменять. Допускаются одинаковые элементы.
# работа со списками https://pythonru.com/uroki/spiski-list-uroki-po-python-dlja-nachinajushhih

thislist = ["Apple", "Banana", "Cocoa"]
print(thislist[1], "#приветики!")
print(thislist[0:2])
thislist[1] = "Blueberry"

# Можно пройтись по списку циклом for и вывести все элементы в списке, один за другим:
print(thislist)
for x in thislist:
    print(x)

print(len(thislist)) #длина списка

# add / добавление элементов списка
thislist.append("Orange") #добавить элемент в список
print(len(thislist))
thislist.insert(1, "Mellow") #добавить элемент в список на 2 позицию
print(thislist)
print(len(thislist))
print(thislist[4])

# delete / удаление элементов списка
thislist.remove("Cocoa") # этот МЕТОД удаляет опред элементы
print(thislist)
del thislist[0] # КЛЮЧЕВОЕ СЛОВО del удаляет опред индекс
print(thislist)
thislist.clear() #метод полностью удаляет список  
print(thislist)
thislist = list(("яблоко", "банан", "вишня"))  #конструктор list() для создания списка, обратите внимание на двойные круглые скобки 
print(thislist)
thislist.sort() #метод сортирует список
print(thislist)

