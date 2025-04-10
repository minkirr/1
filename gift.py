
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Открыть сертификаты 🎁",
            web_app=WebAppInfo(url="https://minkirr.github.io/web/")
        )
    )

    bot.send_message(
        message.chat.id,
        "тут сделать миниапку с 6 картинками и ценами как на их сайте, при нажатии открывается меню с заполнением данных и кнопкой оплатить",
        reply_markup=keyboard
    )
