# открываем файл для записи байтов
with open('file/bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

# читаем как текст
with open('file/bytes.txt', 'r', encoding='ascii') as f:
    # пишем строку байт
    print(f.read())

# открываем файл для записи байтов
with open('file/bytes.txt', 'wb') as f:
    # пишем строку байт
    str = 'Нет войне'
    f.write(str.encode('utf-8'))

# читаем как текст с кодировной utf-8
with open('file/bytes.txt', 'r', encoding='utf-8') as f:
    # пишем строку байт
    print(f.read())
