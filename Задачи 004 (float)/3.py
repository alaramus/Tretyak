'Введите два числа и узнайте их сумму корней,разночть корней, произведение и частное'
import math
num1 = input('Введите число: ')
num2 = input('Введите чилсо: ')
num1 = float(num1)
num2 = float(num2)
print('Сумма корней: ', math.sqrt(num1)+math.sqrt(num2))
print('Разность корней: ', math.sqrt(num1)-math.sqrt(num2))
print('Произведение корней: ', math.sqrt(num1)*math.sqrt(num2))
print('Частное: ', math.sqrt(num1)/math.sqrt(num2))