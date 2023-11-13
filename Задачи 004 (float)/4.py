#Найти длинну окружности если знаешь его площадь
import math
num = float(input('Введите площадь круга: '))
print('Длинна окружности равна: ', math.sqrt(num*4*math.pi))