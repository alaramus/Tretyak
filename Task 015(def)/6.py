def year(leap_year):
    if leap_year % 365 == 0:
        return ('Обычный год')
    else:
        return ('Високосный год')


while True:
    num = int(input('Введи количество дней: '))
    if num in range(365,367):
        print(year(num))
        break
    else:
        print('Введите число 365 или 366')