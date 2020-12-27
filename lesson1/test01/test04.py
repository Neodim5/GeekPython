number = input("Enter number: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)