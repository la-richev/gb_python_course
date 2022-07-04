# Tuple (кортеж) — последовательность, которая упорядочена, но не изменяемая. Допускаются одинаковые элементы.
# https://pythonru.com/uroki/kortezhi-tuple-uroki-po-python-dlja-nachinajushhih

thistuple = ("помидор", "огурец", "лук")
print(thistuple)

# Можно пройтись по списку циклом for и вывести все элементы в кортеже, один за другим:
for x in thistuple:
    print(x)

print(len(thistuple)) #считает длину кортежа

# поиск:
x = thistuple.count("помидор") #Возвращает количество раз, которое указанный элемент встречается в кортеже
print(x)

x = thistuple.index("помидор") #Ищет кортеж по указанному значению и возвращает его индекс
print(x)