import random
from random import randint

def random_list():
    my_list = []
    for i in range(1, 9):
        my_list.append(randint(1, 100))
    print(f'Cгенерированный список: {my_list}')
    return my_list

def choice_list():
    my_list = random_list()
    if len(my_list) > 0:
        result = random.choices(my_list, k=1)
        print(f'Случайно выбранное число из списка: {result}')
    else:
        result = None
    return result

# решение преподавателя
def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result
    # else:
    #     return None 
    # В Python, если мы ничего не возвращаем, то будет возвращаться None

if __name__ == '__53_hw_mod__':
    choice_list()
    print(get_random([1, 2, 3, 4]))
    print(get_random([]))

