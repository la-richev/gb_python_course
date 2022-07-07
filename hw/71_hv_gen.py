# 1. Решить с помощью генераторов списка.
# 1: Даны два списка фруктов. 
# Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

fruit_1 = ['Orange', 'Apple', 'Mango', 'Banana', 'Grape', 'Pear']
fruit_2 = ['Cherry', 'Mango', 'Lemon', 'Kivi', 'Fig', 'Banana', 'Coconut', 'Apricot', 'Grape', 'Pear']
print(type(fruit_1))

# 1
result = set(fruit_1) & set(fruit_2)
print(type(result))
print(result)

for x in result:
    print(x)

# 2
fruits = fruit_1 + fruit_2
result = []
for fruit in fruits:
    if fruits.count(fruit) > 1:
        result.append(fruit)

print(set(result))

# 3 Через генератор
fruits = fruit_1 + fruit_2
result = [fruit for fruit in fruits if fruits.count(fruit) > 1] 
print(set(result))

# 4 Только уникальные элементы
fruits = fruit_1 + fruit_2
result = []
for fruit in fruits:
    if fruit not in result:
        result.append(fruit)

print(result)