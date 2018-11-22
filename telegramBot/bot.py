import os
import sys

import telebot
from telebot import types
from telebot.types import Message
from telebot import apihelper
import config

from geopy.distance import vincenty
from geopy.geocoders import Nominatim

# TOKEN = os.environ.get('BOT_TOKEN')
# PROXY = os.environ.get('PROXY')

# apihelper.proxy = {'https': config.PROXY}
# apihelper.proxy = {'http': 'http://10.10.1.10:3128'}

bot = telebot.TeleBot(config.TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=3)
btn_address = types.KeyboardButton('Адреса магазинов',
                                   request_location=True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_address, btn_payment, btn_delivery)

markup_inline_payment = types.InlineKeyboardMarkup()
btn_in_cash = types.InlineKeyboardButton('Наличный расчет', callback_data='cash')
btn_in_card = types.InlineKeyboardButton('По карте', callback_data='card')
btn_in_transfer = types.InlineKeyboardButton('Перевод', callback_data='transfer')

markup_inline_payment.add(btn_in_cash, btn_in_card, btn_in_transfer)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '{}, Добро пожаловать в лучший Интернет-магазин!'.format(message.from_user.first_name))


@bot.message_handler(func=lambda message: True)
def echo_all(message: Message):
    if message.text == 'Способы доставки':
        bot.reply_to(message, 'Транспортная компания/Почта России/Самовывоз'
                     , reply_markup=markup_menu)
    elif message.text == "Способы оплаты":
        bot.reply_to(message, 'В сети магазинов Cozy kitchen доступны следующие способы оплаты:'
                     , reply_markup=markup_inline_payment)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True, content_type=['location'])
def shop_location(message: Message):
    lon = message.location.longitude
    lat = message.location.latitude
    geolocator = Nominatim()

    if geolocator.reverse(lon, lat).address[-2:] == 'РФ':
        distance = []
        for m in config.SHOPS:
            distance.append(vincenty((m['latm'], m['lonm']), (lon, lat))).kilometers
        index_min = distance.index(min(distance))

        bot.send_message(message.chat.id, "Ближайший к Вам магазин 'Cozy kitchen'")
        bot.send_venue(message.chat.id,
                       config.SHOPS[index_min]['latm'],
                       config.SHOPS[index_min]['lonm'],
                       config.SHOPS[index_min]['title'],
                       config.SHOPS[index_min]['address'],
                       )
    else:
        bot.send_message(message.chat.id, "Извините, доставка осуществляется только в пределах РФ!")


# @bot.message_handler(func=lambda message: True)
# def upper(message: Message):
#     bot.reply_to(message, message.text.upper())

@bot.callback_query_handler(func=lambda call: True)
def callback_payment(call):
    if call.data == 'cash':
        bot.send_message(call.message.chat.id, text="""
        Касса. Оплата принимается в рублях
        """, reply_markup=markup_inline_payment)
    elif call.data == 'card':
        bot.send_message(call.message.chat.id, text="""
        Укажите номер вашей карты 
        """, reply_markup=markup_inline_payment)
    elif call.data == 'transfer':
        bot.send_message(call.message.chat.id, text="""
        Укажите номер счета 
        """, reply_markup=markup_inline_payment)


bot.polling(none_stop=True, timeout=123)
