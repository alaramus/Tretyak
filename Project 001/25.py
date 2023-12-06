def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def write_fibonacci_to_file(n, filename):
    result = fibonacci(n)
    with open(filename, 'w') as file:
        file.write(f'n={n} is: {result}')


filename = 'fibonacci_result.txt'
write_fibonacci_to_file(10, filename)
