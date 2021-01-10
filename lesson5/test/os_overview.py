import os

#if os.path.exists('data.txt'):

# os.remove('data.txt')
current_dir = '.'

files = os.listdir(current_dir)
# print(files)

for x in files:
    print(os.path.split(x))
    #print(os.path.dirname(x))
   #print(os.path.dirname(f"./{x}"))
    #print(os.path.dirname(f"./{x}"))

print(os.path.split(r'c:\temp'))

print(os.path.join('c:\\temp', 'file', 'temp2', '3.txt'))
