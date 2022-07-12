# функция создания файла
def create_file(name, text=None): #если текст не будет задан, тогда мы не будем записывать ничего
    with open(name, 'w', encoding='utf-8') as f: # используем менеджер контекста и сохраняем файл в переменную f
        if text: # если у нас есть текст
            f.write(text) # мы в наш файл будет записывать текст
# если текст нет, после того как закроется менеджер контекста, файл будет создан и закрыт


if __name__ == '__main__': # чтобы при ипорте в др скрипт этот код не выполнялся
    create_file('file_manager/text.dat', 'some text')
    create_folder('file_manager/new_f')
