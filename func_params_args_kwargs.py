def hello_max():
    print('Hello', 'Dim')

hello_max()

# заменим имя параментром
def hello(who):
    print('Hello', who)

hello('Leo')

# заменим обращение
def greeting(who, say):
    print(say, who)

who = input('Что хочешь сказать: ')
say = input('Назови имя человека: ')

greeting(who, say)


def greeting(who, say='Hello'):
    print(say, who)

greeting('Leo')

# args_kwargs
def greeting(say, *who): # параметр со * принято называть args (приходит кортеж)
    print(say, who)

greeting('Hi', 'Leo')

greeting('Hi', 'Leo', 'Max')
greeting('Hi', 'Leo', 'Max', 'Kate')

def get_person(**kwargs): # параметр с ** принято называть kwargs (приходит словарь)
    for k, v in kwargs.items(): # k и v - это ключ и значения из словаря
        print(k, v)

get_person(name='leo', age=20, has_car=True)

