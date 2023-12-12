import telebot
import webbrowser
from telebot import types
import re
bot = telebot.TeleBot('6245865213:AAFG4EK6rolWkB4GHzJxLkK3T0jMGTW3vbQ')

@bot.message_handler(commands=['end'])
def end(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Переход по внешней ссылке!')
    markup.row(btn1)
    btn2 = types.KeyboardButton(text='Удалить!')
    btn3 = types.KeyboardButton(text='Изменить текст!')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Переход по внешней ссылке!':
        webbrowser.open('https://www.google.com/')
    elif message.text == 'Удалить!':
        bot.delete_message(message.chat.id, message.message_id - 2)
    elif message.text == 'Изменить текст!':
        bot.edit_message_text('Edit text', message.chat.id, message.message_id)

@bot.message_handler(commands=['button'])
def buttons(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Переход по внешней ссылке!', url='https://www.google.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Удалить!', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='Изменить текст!', callback_data='edit')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'кнопка', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    hello = f'Привет, {message.from_user.first_name}! Я простой чат-бот. Если у вас есть вопросы, используйте команду /help.'
    bot.send_message(message.chat.id, hello)

@bot.message_handler(commands=['parse'])
def parse(message):
    bot.send_message(message.chat.id, '<b>Жирный текст</b> <em><u>Курсив и подчеркнуто</u></em>', parse_mode='html')

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = f'Список команд:\n\n/start - Приветствие\n/hello - Приветствие\n/help - Помощь\n/info - Информация\n/web - Сайт'
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id,message)

@bot.message_handler(commands=['web'])
def web_message(message):
    webbrowser.open('https://www.google.com/')

@bot.message_handler(content_types=['photo'])
def photo_message(message):
    bot.reply_to(message, 'Красиво!')

@bot.message_handler(commands=['jpg'])
def photo_message(message):
    file = open('krasivye-kartinki-zakaty-59-1402811364.jpg', 'rb')
    bot.send_photo(message.chat.id, file)

@bot.message_handler()
def input_text(message):
    if message.text.lower() == 'пока':
      bot.send_message(message.chat.id, f'Пока!, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')



bot.polling(non_stop=True)
