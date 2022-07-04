# Дом задание к 2 уроку https://gb.ru/chapters/6296, медкарта

f_name = input("Введите имя")
l_name = input("Введите фамилию")
age = int(input("Введите возраст"))
weight = int(input("Введите вес"))
#height = int(input("Введите рост"))

if age <= 30 and weight > 50 and weight < 120:
    print("Пациент в хорошем состоянии")
elif age > 30 and age < 40 and (weight < 50 or weight > 120):
    print("Требуется заняться собой")
elif age >= 40 and age < 90 and (weight < 50 or weight > 120):
    print("Требуется врачебный осмотр")
else:
    print("санитаров!")
