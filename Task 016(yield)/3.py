def genf():
    s = 7
    for i in [1, 2, 3, 4, 5]:
        yield i
        print(s)
        s = s*10+7


g = genf()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('-----------------------------')
for i in genf():
    print(i)
