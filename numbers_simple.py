# output of numbers from 0 to 100
# output of numbers from 0 to n
# output of even numbers from 0 to n (четные)

number = 0
n = int(input("Введите n число от 0 до 100: "))
y = int(input("Введите y число от 0 до 100: "))

while number <= n:
    if number % 2 == 0:
        print(number)
    #number = number + 1
    number += 1

# output odd numbers from 0 to n (нечетные)

while number <= y:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

