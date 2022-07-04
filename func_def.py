# Функция простой разделитель

def print_sep(): # объявление функ БЕЗ ПАРАМЕТРОВ
    print('-' * 100)

print_sep() # вызов функ


def print_sep(sep): # объявление функ С 1 ПАРАМЕТРОМ
    print(sep * 100)

print_sep('*')
print_sep('-')

# меняем знак и длину разделителя
def print_sep(sep, sep_len): # объявление функ С 2 ПАРАМЕТРАМИ
    print(sep * sep_len)

print_sep('*', 10)
print_sep('-', 50)

# используем разделитель в тексте
result = print_sep('*', 10)
print(result) # в данном случае, сама функция не имеет возвращаемого значения, поэтому None

# Меняем функцию, чтобы она возвращало значение
def return_sep(sep, sep_len):
    return sep * sep_len

sep = return_sep('x', 20)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)

def some_f():
    return 10

result = some_f()
print(result)

a = some_f
print(a)

print(type(a))
print(a()) # фукция в python является объектом
# мы можем этот объект записать в некоторую переменную, переменная станет функцией и можем вызвать эту функцию
# это означает, что функцию можно сохранить в какую-то переменную

