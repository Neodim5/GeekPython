my_file = open('data.txt', 'w')

if my_file.writable():
    my_file.write("Update\n") # перезапись всего файла

    strings = ['My new\n', 'string\n', "list\n"]
    my_file.writelines((strings))

else:
    print("cant write")

my_file.close()