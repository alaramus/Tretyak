#Программа которая просит ввести два числа и выводит их разность
num1 = int(input('Ваедите число: '))
num2 = int(input('Ваедите число: '))
if num1 > num2:
    print('Разность чисел:',num1-num2)
if num1 < num2:
    print('Разность чисел:',num2-num1)
if num1 == num2:
    print("Числа равны")