'''
1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
'''

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)
print(my_list_1 - my_list_2)
print(sorted(my_list_1 - my_list_2))


'''
Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. 
Склонением пренебречь (2000 года, 2010 года)
'''

data = input("Введите дату в фотмате dd.mm.yyyy: ")
dd = data[:2]
mm = data[3:5]
yyyy = data[6:]
print('Вы ввели дату', dd, mm, yyyy)
day_dict = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье'
}
mounth_dict = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля'
}
print(day_dict[dd],mounth_dict[mm],yyyy)

'''
3: Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
    Примечание. Списки создайте вручную, например так: my_list_1 = [2, 2, 5, 12, 8, 2, 12]
В этом случае ответ будет: [5, 8]

Хорошее решение:
https://pythonim.ru/list/poluchenie-unikalnyh-znacheniy-iz-spiska-v-python?
https://pythobyte.com/python-count-unique-values-in-list-346c1a17/?
'''

my_list = [2, 2, 5, 12, 8, 2, 12]
result = []

# После этого, используя цикл for, мы проверяем наличие определенного элемента в новом созданном списке (result)
for item in my_list:
    # Если элемент отсутствует, он добавляется в новый список с помощью метода append()
    # if item not in result:
    # Если элемент есть в одном числе

    # Метод count проверяет сколько раз число (item) входит в список, если число входит один раз == 1, 
    # он добавляется в новый список с помощью метода append()
    if my_list.count(item) == 1:
        result.append(item)
print(result)
