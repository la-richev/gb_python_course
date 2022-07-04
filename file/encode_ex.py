s = 'Hello world'
sb = s.encode('ascii')

rus = 'Привет Мир'
sb_rus = rus.encode('utf-8')

print(sb)
print(type(sb))

print(sb_rus)
print(type(sb_rus))

rus = sb_rus.decode('utf-8')
print(rus)
print(type(rus))

