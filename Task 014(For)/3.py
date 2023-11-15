# numbers from num1  num2
num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
if num1 < num2:
    for i in range(num1, num2+1):   # num2, num1-1, -1   reverce ?
        print(i)
if num1 > num2:
    for i in range(num2, num1+1):
        print(i)