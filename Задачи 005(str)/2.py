'Узнайте рост человека и напишите какая трость есму нужна в метрах(минимальная и максимальная длиннна трости считается'
'по формуле x*0.6 b x*0.8'
height = float(input("Введите свой рост в метрах: "))
dlina1 = str(height*0.6)
dlina2 = str(height*0.8)
print('Для человека с таким ростом подойдет трость длинной', dlina1+"-"+dlina2)