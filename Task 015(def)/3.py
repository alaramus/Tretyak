# Calc
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

choice = ''

while True:
    choice = input("Выберите действие (+ - * /): ")            # Почему тут ???
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Неправильный ввод")