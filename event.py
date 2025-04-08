from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    bot.send_message(
        message.chat.id,
        "пока без понятия что это, позже",
        reply_markup=keyboard
    )
