import pickle

# открываем файл
with open('file/person.dat', 'rb') as f:
    # сразу пишет объект целиком с помощью pickle
    person = pickle.load(f)

print(person)