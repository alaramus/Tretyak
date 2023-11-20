def season(month):
    if month in (12, 1, 2):
        return ('winter')
    elif month in (3, 4, 5):
        return ('spring')
    elif month in (6, 7, 8):
        return ('summer')
    elif month in (10, 11, 12):
        return ('autumn')
    else:
        return ('Введите от 1 - 12 ')


num = int(input('Введите номер месяца: '))
print(season(num))