from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    bot.send_message(
        message.chat.id,
        "вот решили открыть свое дело вам к нам бла бла бла, миниапка с выбором группы и так же кнопка заполнить форму и передача данных как и везде",
        reply_markup=keyboard
    )
