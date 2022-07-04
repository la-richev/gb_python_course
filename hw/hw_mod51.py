import os

# функция создающая папки
def create():
    for i in range(1, 10):
        new_path = f'dir_{i}'
#       new_path = os.path.join(f'dir_{i}') или так
        os.mkdir(new_path)

# функция удаляющая папки
def delete():
    for i in range(1, 10):
        new_path = f'dir_{i}'
#       new_path = os.path.join(f'dir_{i}')
        os.rmdir(new_path)

if __name__ == '__53_hw_mod__':
    create()
    delete()