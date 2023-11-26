# find all words with a capital letter
import re
text = open('text.txt', 'r', encoding='utf-8')
lines = text.read()
letter = '[а-я]*[А-Я][а-я]*'
# letter = '[a-z]*[A-Z][a-z]*'    how to connect two languages?
for i in lines.split():
    x = re.fullmatch(letter,i)
    if x is not None:
        print(i, end=' ')
