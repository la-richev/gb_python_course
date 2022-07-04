import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека',
              'шайба', 'олимпиада']

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    # 1040 <= ord(letter) <= 1072 | import re
    # 1040 <= ord(letter) and ord(letter) <= 1072
    if len(letter) != 1:  # <>, =, ==, !=
        # print('...')
        continue
    # print('ваша буква:', letter)
    # 5 min -> 20:06 AIR
    if letter in secret_word:  # hit
        pass
    else:  # miss
        pass

    print(''.join(gamer_word))
