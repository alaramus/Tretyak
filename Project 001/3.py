# Find all words that start with a capital letter

def capital_letter(text, char):
    store = []
    for w in text.split():
        if w.startswith(char):
            store.append(w)
        pass
    pass
    return store


text = open('text.txt', 'r', encoding='utf-8')
lines = text.read()
letters = 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
a = capital_letter(lines, letters)
print(a)
