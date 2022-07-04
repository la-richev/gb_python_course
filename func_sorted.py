# НАБОР ЧИСЕЛ
numbers = [1, 3, 5, 11, 5, 7, 15, 9]
# сортировка по возрастанию / sort in ascending order
print(sorted(numbers))
# сортировка по убыванию / sort in descending order
print(sorted(numbers, reverse=True))

# НАБОР СТРОК
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))

cities = [('Moscow', 120000000), ('New York', 9000000), ('Istambul', 16000000)]
print(sorted(cities))

# сортировка по ключу
def by_count(city):
    return city[1]

# передаем key готовую функцию, мы её не вызываем
print(sorted(cities, key=by_count))

# сортировка по ключу как лямбда
print(sorted(cities, key=lambda city: city[1]))