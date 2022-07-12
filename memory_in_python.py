# в Python нет переменных: названия "переменных" хранатся в Stack, значения (данные) в Heap
# https://youtu.be/8GpI0PAGniA

first_name = "Alex"
print(id(first_name)) # ссылка на ячейку оперативной памяти
first_name = "Petr"
print(id(first_name))
print(id(first_name.upper()))

# адреса в оперативной памяти записываются в 16-ричной форме
print(hex(id(first_name)))
print(hex(id(first_name.upper())))

names = ['Alex']
anothet_names = ['Alex']

print(names == anothet_names) # будет True, тк значения одинаковые

print(hex(id(names))) 
print(hex(id(anothet_names)))

print(names is anothet_names) # будет False, сравниваются ячейки памяти

names.append('Jack')
names.append('John')
print(hex(id(names)))
