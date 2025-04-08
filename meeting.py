from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    bot.send_message(
        message.chat.id,
        "есть только 2 типа свидания, миниапка с выбором и оплатой, должен быть свободен целый класс",
        reply_markup=keyboard
    )
