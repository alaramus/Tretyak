def fact(a):
    p=1
    for i in range(1, a+1):
        p = p*i
        yield p

s = fact(10)
print(next(s))        # Не в списке , а по одному, не в памяти!!!
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print('-----------------------------')
for i in fact(10):
    print(i)

