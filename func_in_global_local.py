def my_f(my_var):
    my_var = 999
    print('переменная внутри функции: ', my_var)

a = 1
my_f(a)
print('После выполнения функции', a)

def some_f():
    a = 999
    print('переменная внутри функции:', a)

a = 1
some_f()
print('После выполнения функции', a)

# Глобальные и локальные переменные
global_var = 1

def my_f():
    # локальная переменная
    local_var = 100
    # мы можем использоваться локальную переменную внутри функции
    print(local_var)
    # глобальная переменная, объявлена в модуле
    print(global_var)
    # переменную global_var изменнить нельзя
    # global_var = 999 (нельзя изменить в пределах функции)

my_f()
print(global_var)
# локальную переменную нельзя вывести вне функции

# Но можно изменить значение глобальной переменной, 
# для этого надо в функции нужно указать ключевое слово (но так лучше не делать!)
global_var = 1
def my_f():
    global global_var # ДАЕМ ДОСТУП НА ИЗМЕНЕНИЕ ГЛОБАЛЬНОЙ ПЕРЕМЕННОЙ
    # локальная переменная
    local_var = 100
    # мы можем использоваться локальную переменную внутри функции
    print(local_var)
    # глобальная переменная, объявлена в модуле
    print(global_var)
    # переменную global_var изменнить нельзя
    global_var = 999

my_f()
print(global_var)