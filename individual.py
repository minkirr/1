from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import requests

WEBAPP_URL = 'https://strangepineaplle.github.io/lobzik-web/'

def handle_individual(bot, message):
    # Получаем доступные слоты
    response = requests.get('http://localhost:5000/free_slots')  # Убедись, что Flask запущен
    slots = response.json()

    if not slots:
        bot.send_message(message.chat.id, "Извините, нет доступных слотов для индивидуальных курсов.")
        return

    # Создаем инлайн-кнопки для выбора слотов
    markup = InlineKeyboardMarkup()
    for slot in slots:
        button_text = f"{slot['дата']} - {slot['время']}"
        callback_data = f"{slot['дата']}|{slot['время']}"
        markup.add(InlineKeyboardButton(button_text, callback_data=callback_data))

    bot.send_message(
        message.chat.id,
        "Выберите удобный слот:",
        reply_markup=markup
    )

# Обработка выбора слота
def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: '|' in call.data)
    def handle_slot_selection(call):
        date, time = call.data.split("|")

        # Формируем ссылку на WebApp с параметрами
        url = f"{WEBAPP_URL}?дата={date}&время={time}"

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Перейти к заполнению", web_app=WebAppInfo(url=url)))

        bot.send_message(
            call.message.chat.id,
            f"Вы выбрали:\n📅 {date}\n⏰ {time}\n\nНажмите кнопку ниже, чтобы перейти к заполнению формы:",
            reply_markup=markup
        )
