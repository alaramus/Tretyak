# factorial
def fact(a):
    p=1
    n=[]
    for i in range(1, a+1):
        p = p*i
        n.append(p)
    return n


print(fact(10))

