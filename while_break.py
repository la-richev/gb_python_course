#while and if
x = 1
y = int(input("Введите число от 1 до 10: "))
while x <= 10:
    print(x)
    if x == y:
        break
    x += 1

print("ИГРА УГАДАЙ ИМЯ СОЗДАТЕЛЯ PYTHON")
f_name = None

while f_name != "Guido":
    f_name = input("ВВЕДИ ИМЯ СОЗДАТЕЛЯ PYTHON (on Eng): ")
    if f_name != "Guido":
        print("Попробуйте еще раз")

print("Ура, Вы угадали!!!")

#break
print("ТЕПЕРЬ УГАДАЙ ФАМИЛИЮ СОЗДАТЕЛЯ PYTHON")
l_name = None

while l_name != "Rossum":
    l_name = input("ВВЕДИ ФАМИЛИЮ СОЗДАТЕЛЯ PYTHON (on Eng): ")
    if l_name == "Rossum":
        break
    print("Попробуйте еще раз")

print("Ура, Вы угадали! Это Guido Rossum.")

print("END GAME")

