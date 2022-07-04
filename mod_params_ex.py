import sys, os

def ping():
    print('pong')

# ping()

def hello(name):
    print('Hello', name)

# hello("Di")

def get_info():
    print(os.listdir())

# get_info()

command = sys.argv[1] # вызывает ошибку, если запустить скрипт без параметров
# это можно решить с помощью условий if/else или обработки исключений 

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)

# /usr/local/bin/python3 /Users/postal/Documents/python/mod_params_ex.py name Di 
# /usr/local/bin/python3 /Users/postal/Documents/python/mod_params_ex.py ping 
# /usr/local/bin/python3 /Users/postal/Documents/python/mod_params_ex.py list

