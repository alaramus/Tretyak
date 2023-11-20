def year(leap):
    if leap % 365 == 0:
        return ('Обычный год')
    else:
        return ('Високосный год')

while True:
    leap = int(input('Введи количество дней: '))
    if leap in range(365,367):
        print(year(leap))
        break
    else:
        print('Введите число 365 или 366')