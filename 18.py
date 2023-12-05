# $
import re

word_number = "hellllo123"

pat = re.compile(r'(.*?)(\d+)')      # re.compile создаем шаблон для поиска
nun = pat.match(word_number)         #  .match ищем по шаблону

if nun:
    word = nun.group(1)                  # ($1) Берет первый   (.*?)(\d+)
    number = nun.group(2)                # ($2) берет второй   (.*?)(\d+)

    print(f'Буквы: {word}')
    print(f'Цифры: {number}')
def num(x):
    print(x)
    if x < 0 or x >= 100 :
        return 0
    return num(x+1)

print(num(7))