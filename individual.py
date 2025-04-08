from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import requests

WEBAPP_URL = "https://minkirr.github.io/web/"  # ссылка на твой miniapp

def handle(bot, message):
    try:
        res = requests.get("http://127.0.0.1:5000/free_slots")
        slots = res.json()
    except Exception:
        bot.send_message(message.chat.id, "Ошибка загрузки слотов.")
        return

    if not slots:
        bot.send_message(message.chat.id, "Нет доступных слотов.")
        return

    markup = InlineKeyboardMarkup(row_width=1)
    for slot in slots:
        slot_data = f"{slot['дата']} {slot['время']}"
        btn = InlineKeyboardButton(
            text=slot_data,
            web_app=WebAppInfo(
                url=f"{WEBAPP_URL}?дата={slot['дата']}&время={slot['время']}&tg_id={message.chat.id}"
            )
        )
        markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Выберите дату и время занятий, чтобы перейти к заполнению данных:",
        reply_markup=markup
    )
