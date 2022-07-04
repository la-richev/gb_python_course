# OS

import os

# Имя операционной системы
print(os.name)

# текущая рабочая директория
print(os.getcwd())

# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_folder') # 2й параметр это имя папки которую мы будем создавать

# создаем папку по новому пути
os.mkdir(new_path)
