# Наибольший общий делитель NOD
def get_nod(a, b):
    while a!= b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


x = int(input('first number: '))
y = int(input('second number: '))
print(get_nod(x, y))