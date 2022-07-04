name = input('Введите Имя ')
surname = input('Введите Фамилию ')
age = int(input('Укажите ваш возраст '))
weight = int(input('Укажите Ваш вес '))

if age <= 30 and weight > 50 and weight < 120:
    print('Уважаемый', name, surname, weight, 'вы в относительно хорошей форме!')
elif age > 30 and age < 40 and (weight < 50 or weight > 120):
    print('Уважаемый', name, surname, weight, 'вам необходима диета!')
elif age >= 40 and (weight < 50 or weight > 120):
    print('Уважаемый', name, surname, weight, 'ваше здоровье вызывает опасение обратитесь к врачу!')
else:
    print("санитаров!")



'''
if age <= 30 and weight > 40 and weight < 120:
    print('Уважаемый', name, surname, weight, 'вы в относительно хорошей форме!')
elif age >= 30 and (weight < 40 or weight > 120):
    print('Уважаемый', name, surname, weight, 'вам необходима диета!')
elif age > 40 and (weight < 40 or weight > 120):
    print('Уважаемый', name, surname, weight, 'ваше здоровье вызывает опасение обратитесь к врачу!')
'''