import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека',
              'шайба', 'олимпиада']

# rnd_idx = 19
# secret_word = words_bank[rnd_idx]
secret_word = random.choice(words_bank)
print(secret_word)

# secret_word.len()
gamer_word = ['*'] * len(secret_word)
# print(type(gamer_word))
# print(gamer_word.to_str())
print(''.join(gamer_word))
# print(gamer_word[3])

gamer_word[3] = 'г'
# setter for str? -> fail -> str: immutable -> mutable -> list -> str
# print(gamer_word)
print(''.join(gamer_word))
