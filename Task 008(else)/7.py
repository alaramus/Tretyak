import random
num = random.randint(-100,100)
if num > 0:
    print('Number', num, ' is a positive number')
elif num < 0:
    print('Number', num, 'is a negative number')
else:
    print(num)