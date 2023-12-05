import re

def extract_emails(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')   # .
    emails = email_pattern.findall(text)
    return emails


with open('text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

'''Лалола Лалоу! 
Нужен ответ на письмо от lalola@Laloy-ch.com. 
Отправить копию sergex-lid@dkf.net- это важно'''

print(extract_emails(input_text))
