# all words
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)    # \b Начало или конец слова,w+ все буквы
    return len(words)


text = input('введите текст: ')
word_count = count_words(text)
print(f'Количество слов в тексте: {word_count}')
