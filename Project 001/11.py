import random

def generate_random(size, lower, upper):
    random_num = []
    for i in range(size):
        random_num.append(random.randint(lower, upper))
    return random_num

def revers_random(arr1):
    arr2 = []
    arr2 = arr1[::-1]
    return arr2


array_size = int(input('Количество случайных чисел: '))
lower = int(input('Минимально доступное число: '))
upper = int(input('Максимально доступное число: '))
arr1 = generate_random(array_size, lower, upper)
print(f"{array_size} случайных чисел от {lower} до {upper}: ", arr1)
arr2 = revers_random(arr1)
print(arr2)