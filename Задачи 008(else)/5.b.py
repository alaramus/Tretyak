# Программа материальной помощи. Если больше 10000 вычесть 1000 налогов и вывести итоговый результат. Если меньше добавить 500 и убрать налог
mn = int(input('Введите сумму помощи: '))
if mn > 10000:
    print('Итоговая сумма', mn -1000)
elif mn < 10000:
    print('Итоговая сумма', mn +500)
else:
    print('Итоговая сумма', mn)