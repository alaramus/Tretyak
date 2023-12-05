import decimal

def formulaFibWithDecimal(n):
    decimal.getcontext().prec = 300000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

num = formulaFibWithDecimal(1000000)
de = len(str(num))
print(de)
print(num)