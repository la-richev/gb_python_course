# Создать модуль music_serialize.py. 
# В этом модуле определить словарь для вашей любимой музыкальной группы...
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, 
# вывести результаты в терминал. 
# Записать результаты в файлы group.json, group.pickle соответственно. 
# В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {
    'Name': 'Г.М.О.',
    'Tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]
    }

print(my_favourite_group)
print(type(my_favourite_group))

# преобразуем словарь в json
json_favourite = json.dumps(my_favourite_group)
print(json_favourite)
print(type(json_favourite))

# преобразуем словарь в байты
bytes_favourite = pickle.dumps(my_favourite_group)
print(bytes_favourite)
print(type(bytes_favourite))

# преобразуем списки любимых групп (словарь) в json и сохраняем в файл
with open('hw/group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

# обратно из файла в объект (проверяем правильность)
with open('hw/group.json', 'r') as f:
    favourite_from_json = json.load(f)

print(favourite_from_json)
print(type(favourite_from_json))
print('Done')

# открываем файл
with open('hw/group.pickle', 'wb') as f:
    # сразу пишет объект целиком с помощью pickle
    pickle.dump(my_favourite_group, f)

print('Объект записан')