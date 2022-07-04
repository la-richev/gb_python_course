import pickle
import json

# открываем "бинарный" файл записаный с помощью pickle
with open('hw/group.pickle', 'rb') as f:
    pickle_favourite = pickle.load(f)

print(pickle_favourite)

# обратно из файла в объект (проверяем правильность)
with open('hw/group.json', 'r', encoding='utf-8') as f:
    favourite_from_json = json.load(f)

print(favourite_from_json)
print(type(favourite_from_json))
print('Done')