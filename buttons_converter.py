from telebot import types

def choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = types.KeyboardButton('USD')
    eur = types.KeyboardButton('EUR')
    kb.add(usd, eur)
    return kb