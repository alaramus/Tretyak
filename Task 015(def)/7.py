def season(month):
    if month in (12, 1, 2):    # Почему не в кавычках?
        return ('winter')
    elif month in (3, 4, 5):
        return ('spring')
    elif month in (6, 7, 8):
        return ('summer')
    elif month in (9, 10, 11):
        return ('autumn')
    else:
        return ('Введите от 1 - 12 ')

while True:
    num = int(input('Введите номер месяца: '))
    if num in range(1, 13):
        print(season(num))
        break
    else:
        print('Введите от 1 - 12')