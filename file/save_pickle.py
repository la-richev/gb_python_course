import pickle

person = {'name': 'Max', 'phones': [123, 345]}

# открываем файл
with open('file/person.dat', 'wb') as f:
    # сразу пишет объект целиком с помощью pickle
    pickle.dump(person, f)

print('Объект записан')