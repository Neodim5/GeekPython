with open('data.txt', 'w') as printable:
    strings=["Dmitry", "Oxana"]
    #print('Hello', file=printable)
    for x in strings:
        print(x, file=printable)

