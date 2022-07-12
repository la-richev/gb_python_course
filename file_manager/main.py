import sys # чтобы получить параметры скрипта
from core import create_file, create_folder, get_list_param, delete_file, copy_file, save_info, change_dir
from guess_game import guess_game

save_info('Start')
# первый параметр это текущий файл #0
# вротой параметр это команды

try:
    command = sys.argv[1]
except IndexError:
    print('Это консольный менеджер. Введите команду help, что бы увидеть список доступных команд. ')
else:
    if command == 'list':
        get_list_param()
    elif command == 'create_file':
        try:
            name = sys.argv[2] # 2 - сл параметр который пойдет после названия ф-ции
        except IndexError: # если не вводится 2й параметр
            print('Отсутствует название файла')
        else: # если все хорошо
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Отсутствует название файла или папки, которую надо удалить')
        delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except ImportError:
            print('Остутствует информация для копирования')
        else:
            copy_file(name, new_name)
    elif command == 'change':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Необходимо ввести имя папки')
        else:
            change_dir(name)
    elif command == 'game':
        guess_game()
    elif command == 'help':
        print('Доступные команды: \n create_file \n create_folder \n delete \n copy \n help')
        print('Пример ввода: ~ python3 main.py [1] [2]')
save_info('End')

# Пример вызова функции без обработчика ошибок (исключений)
# elif command == 'copy':
#     name = sys.argv[2]
#     new_name = sys.argv[3]
#     copy_file(name, new_name)