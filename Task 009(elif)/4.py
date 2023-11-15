# The program is given two numbers and it must tell whether their product is positive, negative, or whether it is zero.
num1 = int(input('type a number : '))
num2 = int(input('type a number : '))
if num1*num2 > 0:
    print(num1*num2, "positive number")
elif num1*num2 < 0:
    print(num1*num2, "negative number")
else:
    print('0')
