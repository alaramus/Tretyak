# The user makes a deposit for a period of years at 10% per annum (every year the size of his deposit increases by 10%.
# This money is added to the deposit amount, and there will also be interest on it next year).
# Write a function bank that takes arguments a and years and returns the amount that will be in the user's account.
def bank(a, y):
    for i in range(y):
        a = a + (a*0.1)
        return a


num = int(input('Сумма: '))
num1 = int(input('Год: '))
print(bank(num, num1))