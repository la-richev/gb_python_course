import json

friends = [
    {'name': 'Max', 'age': 33, 'phones': [123, 345]},
    {'name': 'Kate', 'age': 21}
]

# проверим тип
print(type(friends))

# Открываем файл
with open('file/friends.json', 'w') as f: # w - режим записи
    # преобразуем списки друзей в json и сохраняем в файл
    json_friends = json.dump(friends, f)

# обратно из файла в объект
with open('file/friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))


favourite_tracks = [
    {'name': 'Smack my bitch up', 'artist': 'The Prodigy'},
    {'name': 'XXXXX', 'artist': 'YYYYY'},
    {'name': 'Русская песнь', 'artist': 'Русский артист'}
]

with open('file/tracks.json', 'w', encoding='utf-8') as f: # w - режим записи
    # преобразуем списки друзей в json и сохраняем в файл
    json.dump(favourite_tracks, f)

print('Done')