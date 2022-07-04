# Множества — неупорядоченная и не индексируемая последовательность. Значения не повторяющиеся (повторяющиеся удаляются)

# Они не упорядочены, поэтому элементы будут отображаться в произвольном порядке
thisset = {"лук", "петрушка", "apple"}
print(thisset)

# Множество хранит только уникальные элементы
thisset = {"лук", "петрушка", "apple", "лук"}
print(thisset)
print(len(thisset))
print(type(thisset))

cart = ["лук", "петрушка", "apple", "лук"]
print(type(cart))
cart = set(cart)
print("новый тип: ", type(cart))

# Можно пройтись по списку циклом for и вывести все элементы в множестве, один за другим:
for x in thisset:
    print(x)

# поиск
print("apple" in thisset) #Проверим присутствует ли "dict" этой последовательности

# Можно добавить элемент с помощью метода add 
thisset.add("мяу")
print(thisset)

# Можно добавить НЕСКОЛЬКО элементов с помощью метода update
thisset.update(["orange", "banana"])
print(thisset)
print(len(thisset))

# Удалить
thisset.discard('apple')
print(thisset)
print(len(thisset))

thisset.pop() #удалить последний элемент (неизвестно какой)
print(thisset)
print(len(thisset))

# Объединение
thisset_2 = {"серянь", "мысо", "греча", "лук", "картошка", " orange"}
x = thisset.union(thisset_2)
print(x)
print(len(x))

thisset_3 = {"серянь", "мысо", "береза"}
x.symmetric_difference_update(thisset_3) # возвращает непересекающиеся элементы во множестве
print(x)
print(len(x))

# in проверить наличие во множестве и сразу вывести
print("петрушка" in thisset)

# for
for set in thisset:
    print(set)