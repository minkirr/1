
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def handle(bot, message):
    # Создаём инлайн-клавиатуру с WebApp-кнопкой
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Открыть сертификаты 🎁",
            web_app=WebAppInfo(url="https://minkirr.github.io/web/")
        )
    )

    # Отправляем сообщение с кнопкой
    bot.send_message(
        message.chat.id,
        "тут сделать миниапку с 6 картинками и ценами как на их сайте, при нажатии открывается меню с заполнением данных и кнопкой оплатить",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['web_app_data'])
 async def web_app(message: types.Message):
   await message.answer(message.web_app_data.data)
