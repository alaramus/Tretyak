#Введите число и узнайте чему равен его корень квадратный и его квадрат
import math
num = input('Введите число: ')
num = float(num)
print('Квадрат числа', num, 'равен',num**2, ',а квадратный корень равен', math.sqrt(num))