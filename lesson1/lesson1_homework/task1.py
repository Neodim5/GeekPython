__author__ = 'Neklyudov Dmitry'

# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = input("Enter your name: ")
print("Hello, %s!" % name)
access = False
password_orig = "pa$$w0rd"
password = input("введите пароль >>> ")

while access == False:
    if password_orig == password:
        print("Верно")
        access = True
    else:
        print("не верно")
        access = False

age = int(input("введите ваш возвраст >>>"))

if age >= 14:
    print(f"Ваш врозвраст {age}. Паспорт можно получить")
    if 20 >= age < 45:
        print(f"Ваш врозвраст {age}. Паспорт пора сменить")
elif age < 1:
    print("УПС!")
else:
    print(f"Ваш врозвраст {age}. Паспорт нельзя получить")
