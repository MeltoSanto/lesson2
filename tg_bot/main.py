import time
import telebot
import vk_api
import config
import random
from telebot import types


bot = telebot.TeleBot(config.tg_tkn)


@bot.message_handler(commands=["start"])
def start(m, res = False):
    # pht = open('media/photo_1.png', 'rb')
    # bot.send_photo(m.chat.id, pht)

    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('1️⃣')
    btn2 = types.KeyboardButton('2️⃣')

    marcup.add(btn1, btn2)

    c_id = str(m.chat.id)
    bot.send_message(m.chat.id, "Привет, {0.username}, я бот <b>{1.first_name}</b>!\n"
                                "Мой id: ".format(m.from_user, bot.get_me()) + c_id, parse_mode='html',
                                reply_markup=marcup)
a = []
@bot.message_handler(commands=["help"])
def help(m, res = False):
    if a == None:
        bot.send_message(m.chat.id, "Список пуст.")
    else:
        b = ", ".join(a)
        bot.send_message(m.chat.id, b)
        # pht = open('media/photo_1.png', 'rb')
        # bot.send_photo(m.chat.id, photo=pht)


@bot.message_handler(content_types=["text"])
def handle_text(m):
    if m.text == '1️⃣':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('🤘', callback_data='good')
        btn2 = types.InlineKeyboardButton('🤙', callback_data='so_good')
        markup.add(btn1, btn2)

        bot.send_message(m.chat.id, 'А круто ты это придумал!', reply_markup=markup)
    elif m.text == '2️⃣':
        bot.send_message(m.chat.id, "Я сначала даже и не понял.")
    else:
        bot.send_message(m.chat.id, "Ой, а чё делать?")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.m:
            if call.data == 'good':
                bot.send_message(call.m.chat.id, "Good")
            elif call.data == 'so_good':
                bot.send_message(call.m.chat.id, "So good")
            else:
                bot.send_message(call.m.chat.id, "No")

    except Exception as e:
        print(repr(e))

# @bot.message_handler(commands=["help"])
# def help(m, res=False):
#     bot.send_message(m.chat.id, "У меня есть такие команды:")



bot.polling(none_stop=True, interval=0)


