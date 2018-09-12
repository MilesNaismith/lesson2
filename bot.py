from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from tokentoken import API_TOKEN
import ephem
from datetime import datetime, date, time

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


def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_user))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

main()