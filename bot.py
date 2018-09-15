from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from tokentoken import API_TOKEN
#import ephem
from datetime import datetime, date, time
import telegram

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = 'Привет! Бот работает!'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_user(bot,update):
    user_text = update.message.text.split()
    planet = user_text[1]
    today = datetime.strftime(datetime.now(), '%Y/%m/%d')
    planet = getattr(ephem,planet)(today)
    text = ephem.constellation(planet)
    print(text)
    update.message.reply_text(text)

def word_count(bot, update):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        text = 'Требуется ввести фразу'
    elif len(user_text) == 2 and user_text[1] =='""':
        text = 'Вы просто написали кавычки'
    elif len(user_text) == 2 and user_text[1] =='"':
        text = 'Вы просто написали кавычку'            
    elif user_text[1].startswith('"') and user_text[-1].endswith('"'):
        text = str(len(user_text) - 1)
        if text.endswith('1'):
            text = text + ' слово'
        elif text.endswith('2') or text.endswith('3'):
            text = text + ' слова'
        else:
            text = text + ' слов'        
    else:
        text = 'Где кавычки?'        
    print(text)
    update.message.reply_text(text)   

def bot_calc(bot, update):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        answer = 'Что будем считать? Отсутствует выражение!'
        print(answer)
        update.message.reply_text(answer)
    elif len(user_text) > 2:
        answer = 'Неверный формат, уберите пробелы в выражении'
        print(answer)
        update.message.reply_text(answer)
    else:
        text = user_text[1]

    if '+' in text:
        x = int(text[:text.index('+')])
        y = int(text[text.index('+') + 1:text.index('=')])
        answer = x + y
    elif '-'in text:
        x = int(text[:text.index('-')])
        y = int(text[text.index('-') + 1:text.index('=')])
        answer = x - y
    elif '*' in text:
        x = int(text[:text.index('*')])
        y = int(text[text.index('*') + 1:text.index('=')])
        answer = x * y
    elif '/' in text:
        x = int(text[:text.index('/')])
        y = int(text[text.index('/') + 1:text.index('=')])
        if y == 0:
            answer = 'на ноль делить нельзя'
        else:
            answer = x / y       
    print(answer)
    update.message.reply_text(answer)            

def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_user))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(CommandHandler('calc', bot_calc))
    dp.add_handler(CommandHandler('keyboard', calc_keyboard))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

main()