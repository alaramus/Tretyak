#Программа материальной помощи. Если больше 10000 вычесть 1000 налогов и вывести итоговый результат. Если меньше добавить 500 и убрать налог
mon = int(input('Введите сумму помощи: '))
if mon > 10000:
    print('Итоговая сумма',mon -1000)
if mon < 10000:
    print('Итоговая сумма',mon +500)
if mon == 10000:
    print('Итоговая сумма',mon)


#else не нужен потому что 3 варианта? уточнить...