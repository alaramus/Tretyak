# сгенерировать  список фибоначе
def fibonacci(num):
    sequence = [0, 1]                                           #список, который начинается с первых двух чисел фибоначчи
    while len(sequence) < num:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def number(num):
    current_index = 1
    arr2 = []
    while current_index <= num:
        arr2.append(current_index)
        current_index = current_index + 1
    return arr2


num = int(input('Введите количество элементов числовой последовательности: '))

fibonacci_list = fibonacci(num)

print('Элементы числовой последовательности: ', fibonacci_list)
print('Порядковый номер в последовательности:',number(num))
