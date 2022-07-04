import sys

# sys.argv и sys.path рассмотрим подробнее далее

# путь до интерпритарора
print(sys.executable)

# инфа о платформе
print(sys.platform)

# выход из python
#sys.exit()

print('Этот код мы уже не выполним')

# sys.path оч важная переменная, она хранит пути по которым пайтон хранит модули
# ЭТО СПИСОК
print(type(sys.path))
for p in sys.path:
    print(p)

# импортируем модуль откуда-н из другого места
sys.path.append('/Users/postal/') # работаем как с обычным листом
# путь к файлу в терминале можно узнать командой pwd
import mymodule

print(type(sys.path))
for p in sys.path:
    print(p)