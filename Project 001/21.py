import re

def extract_emails(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(text)
    return emails


input_text = input('введите текст: ')

'''input_text = Лалола Лалоу! 
Нужен ответ на письмо от lalola@Laloy-ch.com. 
Отправить копию sergex-lid@dkf.net- это важно'''

found_emails = extract_emails(input_text)

print(found_emails)

#Лалола Лалоу!
#Нужен ответ на письмо от lalola@Laloy-ch.com.
#Отправить копию sergex-lid@dkf.net- это важно

# Лалола Лалоу! Нужен ответ на письмо от lalola@Laloy-ch.com. Отправить копию sergex-lid@dkf.net- это важно