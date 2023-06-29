import time
import telebot
import vk_api
import config
import random
from telebot import types
from funk import *


bot = telebot.TeleBot(config.tg_tkn)



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, это бот для просмотра статистики.\nДля начала введи /get или нажми 'Задать ID'")


@bot.message_handler(commands=["get"])
def get(message):
    msg = bot.send_message(message.chat.id, 'Введи свой ID:')
    bot.register_next_step_handler(msg, start_2)


def start_2(message):
    global you_id
    you_id = message.text
    bot.send_message(message.chat.id, f'Твой ID: {you_id}')

@bot.message_handler(commands=["rep"])
def rep(message):
    bot.send_message(message.chat.id, f'ID: {you_id}')


@bot.message_handler(commands=["five"])
def ten_best(message):
    ten_rating_fr(bot, message, you_id)


@bot.message_handler(commands=["mypl"])
def my_place(message):
    my_place_in_ten_rating_fr(bot, message, you_id)


@bot.message_handler(commands=["post"])
def posts(message):
    more_all_posts(bot, message, you_id)


@bot.message_handler(commands=["cool"])
def cool_id(message):
    cool_id_at_friends(bot, message, you_id)





bot.polling(none_stop=True)