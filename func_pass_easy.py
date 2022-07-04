# def print_sep(sep, sep_len):
#     print(sep * sep_len)

# sep = input('Задайте значек: ')
# sep_len = int(input('Задайте длину: '))

# print_sep(sep, sep_len)


# def return_sep(sep, sep_len):
#     return sep * sep_len

# print('Это слово длинной', len(text), 'букв')
# question = f'Пароль: {sep_len}'
# print(question)

def print_sep(sep, sep_len):
    print(sep * sep_len)

text = input('Введите секретное слово: ')
sep = input('Задайте значек: ')
sep_len = int(len(text))

print_sep(sep, sep_len)