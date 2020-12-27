# f строка

ip = '192.168.1.4'
mask = 10

print(f"ip-params: {ip}, mask: {mask}")

# Помимо подстановки значений переменных, в фигурных скобках допустимо написать выражение

octets = ['10', '1', '1', '1']
mask = 10

print(f"ip-params: {'.'.join(octets)}, mask: {mask}")

# Через f-строки также возможен вывод столбцами с одинаковым расстоянием между ними.

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''IP address: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}''')


def to_lowercase(input):
    return input.lower()


name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
# вызов напрямую
print(f"{name.lower()} is funny.")
