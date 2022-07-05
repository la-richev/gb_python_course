# слово -> СлОвО

word = 'слово'
result = []

for i in range(len(word)):
    if i%2 != 0: # если индекс делится на 2 без остатка
        letter = word[i].lower() # если буква четная 
    else:
        letter = word[i].upper()
    result.append(letter)

print(type(letter))

result = ''.join(result)    # из списка сделать строчку метод join
print(result)

# с тернатным оператором
word = 'слово'
result = []

for i in range(len(word)):
    letter = word[i].lower() if i%2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)    # из списка сделать строчку метод join
print(result)