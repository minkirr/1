
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    bot.send_message(
        message.chat.id,
        "тут заполнение формы номер курс и тд и передача администратору",
        reply_markup=keyboard
    )
