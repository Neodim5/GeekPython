# простой способ импорта модуля
import my_functions

my_functions.show_msg()
print(my_functions.simple_calc())

# второй способ импорта модуля
from my_functions import show_msg
from my_functions import simple_calc

show_msg()
print(simple_calc())
