import random
num = random.randint(0,1000)
if num > 500:
    print(num, "Значит летим на луну")
elif num < 500:
    print(num, "Закапываем")
else:
    print("Думае что с этим делать")