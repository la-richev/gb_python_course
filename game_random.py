import random

words_bank = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада']

secret_word = random.choice(words_bank) #random не подойдет для криптографии
print(secret_word)

gamer_word = "*" * len(secret_word) #функция len (утиная типизация) 37 мин: https://gbcdn.mrgcdn.ru/uploads/record/139680/attachment/1e87e3173f6971dd6dadd4aeac0b3f8a.mp4
print(gamer_word)

gamer_word[3] = ""