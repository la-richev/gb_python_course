from doctest import testmod
from unicodedata import name
import firstmodul
from mod.testmod import name, bar

print(f'{name} сказал:')
print(firstmodul.text)

bar()