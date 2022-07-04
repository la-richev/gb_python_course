import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека',
              'шайба', 'олимпиада']

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_cnt = 0
while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    if len(letter) != 1:
        continue

    if letter in secret_word:
        # hash table: dict or set
        # brute force
        position = 0
        for symbol in secret_word:
            # print(symbol)
            if letter == symbol:
                gamer_word[position] = letter
            position += 1
    else:
        errors_cnt += 1
        # errors_cnt++
        print('ошибок допущено:', errors_cnt)
        if errors_cnt == 8:
            print('вы проиграли')
            break

    print(''.join(gamer_word))
