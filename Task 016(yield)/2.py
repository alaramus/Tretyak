# Выражение -генератор, для больших объектов , не хранит в памяти
def genf():
    for i in [1, 2, 3]:
        yield i

s = genf()                # < Всегда переменная?
print(next(s))
print(next(s))
print('---------------------------------')
for i in genf():
    print(i)