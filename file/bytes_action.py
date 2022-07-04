# str
s = 'Hello world'
# bytes
sb = b'Hello world'

# index in usual str
print(s[1])

# index in bytes str
print(sb[1])

# перебор
for item in sb:
    print(item)

print('\n')
# строка байт
sb = b'Ad'

# по ascii таблице получится 65
print(sb[0])
# по ascii таблице получится 100
print(sb[1])