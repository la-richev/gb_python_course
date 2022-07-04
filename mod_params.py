import sys

print(sys.argv[0])

for arg in sys.argv:
    print(arg)
    print(type(arg))

# в терминале можно вызвать с параметрами python3 mod_no_params.py 1223 dsds 1.33