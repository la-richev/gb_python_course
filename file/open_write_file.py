# октрываем файл на запись - файла не существует
f = open('file/second.txt', 'w')

# открываем файл на чтение - файла не существует
# f = open('second.txt', 'r')

# открываем файл на чтение - файла существует
#f = open('first.txt', 'r')

f.write('Hello\n') # f. - переменная файла + метод write, добавляем перенос строки
f.write('World\n')

f.writelines(['Hello\n', 'world\n'])