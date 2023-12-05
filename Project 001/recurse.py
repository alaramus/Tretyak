def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

def fibonac(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonac(10))

def fibona(n):
    fibo_list = [1, 1]
    for i in range(2, n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list


print(fibona(10))


def fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    li = fib(n-1)
    li.append(li[-1] + li[-2])
    return li


print(fib(10))


def recursiveFib(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFib(n - 1) + recursiveFib(n - 2)

print(recursiveFib(10))


def fibonac(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonac(10))