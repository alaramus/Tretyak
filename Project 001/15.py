# список случайных чисел, вывести те что делятся на три и не на пять
import random
def random_list():
    random_array = []
    for i in range(10):
        random_array.append(random.randint(1, 100))
    return random_array

def numbers(rnd):
    num = []
    for i in random_list():
        if i % 3 == 0 and i % 5 != 0:
            num.append(i)
    return num

rnd = random_list()

print('Список случайных чисел:', rnd)
print('Список чисел которые делятся на 3 и не делятся на 5:', numbers(rnd))
