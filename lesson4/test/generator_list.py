'''
Важно! Генератор создаёт новый список, а не изменяет текущий.
'''

my_list = [2, 4, 6]
new_list = [el + 10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")


my_list = [2, 4, 6]
print(f"Исходный список: {my_list}")
new_list = []
for el in my_list:
   new_list.append(el + 10)
print(f"Новый список: {new_list}")
'''
 В цикле for возможен перебор не только элементов списка, но и строк файла.
'''

lines = [line.strip() for line in open('text.txt')]
print(lines)

'''
В генератор допускается добавление условия.
'''

my_list = [10, 25, 30, 45, 50]
print(my_list)
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)

'''
Допустимо использовать вложенные циклы
'''

str_1 = "abc"
str_2 = "d"
str_3 = "efg"
sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
print(sets)

'''
Здесь мы используем генераторное выражение для элементов кортежа, но в 
результате получаем объект-итератор. Такой результат связан с использованием 
круглых скобок в генераторном выражении. Если в этом примере заменить кортеж 
на список, результат будет идентичный (объект-итератор).

new_obj = [el+10 for el in my_tuple]
'''

my_tuple = (2, 4, 6)
new_obj = (el+10 for el in my_tuple)

print(new_obj)


my_tuple = [2, 4, 6]
new_obj = (el+10 for el in my_tuple)

print(new_obj)
