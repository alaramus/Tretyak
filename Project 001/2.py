# Find all words that start with a capital letter
text = open('text.txt', 'r', encoding='utf-8')
lines = text.read()
letters = 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
# How to write the alphabet from a to z?
for w in lines.split():
     if w.startswith(letters):
        print(w, end=' ')
