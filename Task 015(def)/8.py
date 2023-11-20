import math
num = int(input('Введите сторону квадрата: '))
def square(x):
    perimeter = x * 4
    area = x ** 2
    diagonal = round(x * math.sqrt(2), 2)
    return perimeter, area, diagonal


print(square(num))