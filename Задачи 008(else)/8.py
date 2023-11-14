import random
num = random.randint(0,1000)
if num > 500:
    print(num, "Go to the moon!")
elif num < 500:
    print(num, "Burying the body")
else:
    print("Thinking what to do about it")