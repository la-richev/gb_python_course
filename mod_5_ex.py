# создать 5 подпапок названия которых состоят из названия платформы (sys.platform) и порядкового номера
import sys, os

name = sys.platform # инфа о платформе, выводит название платформы

for i in range(1, 6):
    new_path = os.path.join(f'{name}_{i}') # создаем новый путь os.path.join() до нашего модуля os.getcwd() и название папки
    os.mkdir(new_path) # передаем new_path функции os.mkdir

2
