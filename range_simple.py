numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))

winners = ['Max', 'Leo', 'Di']

# простой перебор
for name in winners:
    print(name)

# использоваться range
for i in range(len(winners)): # переменная индексов будет i тк мы будем перебираться индексы
    print(i)
    print(winners[i])

# # использоваться range (вывод по красоте)
for i in range(len(winners)):
    print(i+1, '-' , winners[i])

for i in range(1, len(winners)+1):
    print(i, '-' , winners[i-1])