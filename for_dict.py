friend = {
    'name': 'Leo',
    'age': 38,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

# по значениям
for val in friend.values():
    print(val)
    print(type(val))

# пары ключ значение
for item in friend.items():
    print(item)
    print(type(item))

for key, val in friend.items():
    print(key)
    print(val)

