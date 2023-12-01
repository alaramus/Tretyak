# сгенерировать  список фибоначе
def fibonacci(n):
    sequence = [0, 1]                                           #список, который начинается с первых двух чисел фибоначчи
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


fibonacci_list = fibonacci(11)
print(fibonacci_list)
