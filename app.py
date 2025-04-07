#API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
#https://strangepineaplle.github.io/lobzik-web/

from flask import Flask, request, jsonify
import json
import threading
import telebot
from telebot.types import ReplyKeyboardMarkup
import individual  # Импортируем файл для индивидуальных курсов

API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
DB_PATH = 'database.json'
WEBAPP_URL = 'https://strangepineaplle.github.io/lobzik-web/'  # ваш Netlify домен

app = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)

# Роут для получения доступных слотов
@app.route('/free_slots', methods=['GET'])
def free_slots():
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        return jsonify([])

    free = [
        {"дата": slot["дата"], "время": slot["время"]}
        for slot in db
        if slot["тип"] == "индивидульный курс" and slot["фио"] == ""
    ]
    return jsonify(free)

# TELEGRAM
def create_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = ["индивидульный курс", "подарить сертефикат", "записатся на интенсив",
               "записатся на мероприятие", "записатся в кофоркинг", "свидание"]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Я бот, выбери услугу:', reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda m: m.text == 'индивидульный курс')
def individual_handler(message):
    individual.handle_individual(bot, message)

# Регистрируем callback-обработчики
individual.register_handlers(bot)


def run_bot():
    print("Бот запущен")
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(debug=True, use_reloader=False)
