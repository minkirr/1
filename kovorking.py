from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    bot.send_message(
        message.chat.id,
        "аренда верстака почасовая принципу занять свободное место, можно записаться на свободное место (если в кабинете мастер класс блокируем класс)",
        reply_markup=keyboard
    )
