# Пара собирается в отпуск
# Ди взял 
di_things = {'Phone', 'Bike', 'Macbook'}
# Кейт 
kate_things = {'Phone', 'Cosmetic', 'Notebook'}

# какие вещи взяла пара
print(di_things | kate_things) #объединяем |

# какие повторяются
print(di_things & kate_things) # пересечения &

# какие взял Ди, но не взяла Кейт
print(di_things - kate_things) # вычетание -

# какие взяла Кейт, но не взял Ди
print(kate_things - di_things)