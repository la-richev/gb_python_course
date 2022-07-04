import json

friends = [
    {'name': 'Max', 'age': 33, 'phones': [123, 345]},
    {'name': 'Kate', 'age': 21}
]

# проверим тип
print(type(friends))

# преобразуем список друзей в json
json_friends = json.dumps(friends)

# печатаем что получилось
print(json_friends)

# проверим тип
friends = json.loads(json_friends)

print(friends)
print(type(friends))