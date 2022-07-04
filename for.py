# Цикл for используется для итерации по последовательности (list, tuple, dict, set или str)

from re import I


fruits = ["banana", "apple", "orange"]
for x in fruits:
    print(x)

for x in "БАНАН":
    print(x)

fruits = ["яблоко", "банан", "вишня"]  
for x  in fruits:
    print(x)
    if x == "банан":
        break

for x in range(10, 25, 5):  
    print(x)

# Цикл for и while

name = 'Max'
friends_name = ['Max', 'Leo', 'Di']
roles = ('admin', 'guest', 'user')

if 'Max' in name:
    print('Yes')

if 'Max' in friends_name:
    print('I have this friends')

#while
print('Цикл while для последовательности (list) friends_name:')
i = 0
while i < len(friends_name):
    friend = friends_name[i]
    print(friend)
    i += 1

#for
print('Цикл for для последовательности (list) friends_name:')
for friend in friends_name:
    print(friend)

print('Цикл for для последовательности (str) name:')
for words in name:
    print(words)

print('Цикл for для кортежа roles:')
for role in roles:
    print(role)
