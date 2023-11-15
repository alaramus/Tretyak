# Print all squares of natural numbers not exceeding the given number A.
a = int(input('Type number: '))
for i in range(1, a+1):
    b = i*i
    if b < 50:
        print(b, end=' ')
    else:
        pass