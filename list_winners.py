# можно объявить пустой список
empty_list = []

# можно объявить список и заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - лист
print(type(friends))
print(len(friends))

friends.append('Ron')
print(friends.pop())

friends.remove('Kate') # удалить по имени
del friends[1] # удалить по индексу
print(friends)

