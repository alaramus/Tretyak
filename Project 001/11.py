'''1. Сгенерировать массив из 20 целых случайных чисел от 2 до 118 включительно  ()
2. Создать новый массив, элементы для которого взять с конца первого массива начиная с последнего 20го элемента с прогрессивным шагом в единицу.
То есть элемент [20], потом (минус 1) [19], далее (уже минус 2), [17], (еще минус 3), [14], (минус 4) [10] и т.д.

arr1 = [4, 34, ....., 110, 11, 40, 27, 83, 75, 31, 22]

arr2 = [22, 31, 83, 11, .... ]'''
import random

def generate_random(size, lower, upper):
    random_num = []
    for i in range(size):
        random_num.append(random.randint(lower, upper))
    return random_num

def generate_sequence(arr1):
    arr2 = []
    step = 1
    arr3 = arr1[::-1]
    current_index = 0
    while current_index < len(arr3):      # while выполняется пока значение current_index меньше  длинне arr3
        arr2.append(arr3[current_index])
        current_index += step             # Индекс увеличивается на текущий шаг.
        step += 1                         # Значение шага увеличивается
    return arr2


array_size = int(input('Количество случайных чисел: '))
lower = int(input('Минимально доступное число: '))
upper = int(input('Максимально доступное число: '))

arr1 = generate_random(array_size, lower, upper)
arr2 = generate_sequence(arr1)

print(f"{array_size} случайных чисел от {lower} до {upper}: ", arr1)
print(f'Элементы массива начиная с {array_size} элемента с прогрессивным шагом в единицу: ', arr2)
