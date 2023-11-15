# сравнить три числа и сказать какое самое большое
num1 = int(input('type a number: '))
num2 = int(input('type a number: '))
num3 = int(input('type a number: '))
if num1 > num2:
    if num1 > num3:
        print(num1, ' the biggest number')
    else:
        print(num3, 'the biggest number')
else:
    if num2 > num3:
        print(num2, 'the biggest number')
    else:
        print(num3, 'the biggest number')