password = input("введите пароль >>> ")
original_password = "123456"
if original_password == password:
    print("Верно")
else:
    print("не верно")

age = int(input("введите ваш возвраст >>>"))

if age >= 14:
    print("паспорт можно получить")
    if 20 >= age < 45:
        print("паспорт пора сменить")
elif age < 1:
    print("Сгыегь")
else:
    print("паспорт нельзя получить")
