#API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
#https://strangepineaplle.github.io/lobzik-web/

from flask import Flask, request, jsonify
import json
import threading
import telebot
from telebot.types import ReplyKeyboardMarkup
import individual

API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
DB_PATH = 'database.json'

app = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    for slot in db:
        if slot['дата'] == data['дата'] and slot['время'] == data['время'] and slot['фио'] == "":
            slot['фио'] = data['фио']
            slot['телефон'] = data['телефон']
            slot['оплата'] = "ожидает оплаты"
            slot['tg_id'] = data['tg_id']
            break
    else:
        return 'Слот не найден или занят', 400

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    return 'Данные сохранены', 200


@app.route('/free_slots', methods=['GET'])
def free_slots():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)
    free = [
        {"дата": s["дата"], "время": s["время"]}
        for s in db
        if s["тип"] == "индивидульный курс" and s["фио"] == ""
    ]
    return jsonify(free)

def create_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("индивидульный курс")
    return markup

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda m: m.text == 'индивидульный курс')
def handle_individual_course(message):
    individual.handle(bot, message)

def run_bot():
    print("Бот запущен")
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(debug=True, use_reloader=False)
