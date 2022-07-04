# открываем файл на чтение - файл существует
f = open('file/first.txt', 'r')

# получим содержимое файла в одну строчку
#print(f.read())

# перебрать построчно с помощью for
# for line in f:
#     print(line)

# но тк при записи файла мы использовали перенос строки, 
# у нас появляется двойной перенос, но его можно убрать заменив символ.
for line in f:
    print(line.replace('\n', ''))

f.close()

# менеджер контекста with
with open('file/first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')