# Find all words that start with a capital letter

def capital_letter(x, y):
    for w in x.split():
        if w.startswith(y):  # ??
            return w


text = open('text.txt', 'r', encoding='utf-8')
lines = text.read()
letters = 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
print(capital_letter(lines, letters))
