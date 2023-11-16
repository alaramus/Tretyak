# biggest from 3 numbers
def get_max(a, b):
    return a if a > b else b

x = int(input('Введите' ))
y = int(input('Введите' ))
z = int(input('Введите' ))
print(get_max(x, get_max(y, z)))