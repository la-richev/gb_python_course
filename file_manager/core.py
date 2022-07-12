import os # нужно для создания папки
import shutil # модуль для копирования папок и файлов
import datetime


# функция создания файла
def create_file(name, text=None): #если текст не будет задан, тогда мы не будем записывать ничего
    with open(name, 'w', encoding='utf-8') as f: # используем менеджер контекста и сохраняем файл в переменную f
        if text: # если у нас есть текст
            f.write(text) # мы в наш файл будет записывать текст
# если текст нет, после того как закроется менеджер контекста, файл будет создан и закрыт


# фунция создания папки с исключением
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError: # быдем отслеживать, если файл уже создан
        print('Такая папка уже есть')


# функция создает список из файлов и папок в текушей директории:
def get_list():
    print(os.listdir()) # or os.listdir('file_manager/')


# функция создает список из файлов и папок в текушей директории c параметрами (поиск папки):
def get_list_param(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)] # os.path.isdir функция проверки на папку
    print(result)


# удаление
def delete_file(name):
    if os.path.isdir(name): #проверка на папку
        os.rmdir(name) # удаление папки 
    else:
        os.remove(name) # удаление файла


# простое создание копии, без обработки исключения
def copy_file_easy(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)


# создание копии, с обработкой исключения
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name) # для того чтобы скопировать файл, ползуемся copy


# вывод времени
def save_info(message):
    current_time = datetime.datetime.now() # текущая дата и текущее время
    result = f'{current_time} - {message}'
    # print(result)
    with open('log.txt', 'a', encoding='utf-8') as f: # a - дозапись
        f.write(result + '\n')


# os.chdir(path) - смена текущей директории.
def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


# os.renames(old, new) - переименовывает old в new, создавая промежуточные директории.


if __name__ == '__main__': # чтобы при ипорте в др скрипт этот код не выполнялся
    create_file('text.dat', 'some text')
    create_folder('new_f')
    get_list()
    get_list_param(True)
    delete_file('new_f')
    copy_file('new1', 'new2')
    copy_file('text.dat', 'text_copy.dat')
    save_info('текущее время')