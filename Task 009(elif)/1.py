# Calc
comand = input('Введите команду: ')
if comand == 'помощь':
    print('Введите одну из команд: ')
    print("+, /, *, -")
elif comand == '+':
    num1 = float(input('Введите первое слагаемое: '))
    num2 = float(input('Введите второе слагаемое: '))
    print(num1,'+',num2,'=',num1+num2)
elif comand == '*':
    num1 = float(input('Введите первый множитель: '))
    num2 = float(input('Введите второй множитель: '))
    print(num1,'*',num2,'=',num1*num2)
elif comand == '/':
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    print(num1,'/',num2,'=',num1/num2)
elif comand == '-':
    num1 = float(input('Введите число: '))
    num2 = float(input('Введите вычитаемое: '))
    print(num1,'-',num2,'=',num1-num2)
else:
    print('Не верная команда')
