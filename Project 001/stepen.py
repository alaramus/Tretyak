def Power(x, y):
    if y>0:
        return x * Power(x, y-1)
    else:
        return 1

x = int(input('число: '))
y = int(input('степень : '))
res = Power(x, y)
print(res)
