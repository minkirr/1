
from flask import Flask, request, jsonify
import json
import threading
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import individual, gift, intense, event, kovorking, meeting


API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
DB_PATH = 'database.json'

app = Flask(__name__)
bot = telebot.TeleBot(API_TOKEN)


def create_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Индивидуальный курс"))
    markup.row(KeyboardButton("подарить сертификат"))
    markup.row(KeyboardButton("интенсив"))
    markup.row(KeyboardButton("мероприятие"))
    markup.row(KeyboardButton("коворкинг"))
    return markup

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=create_main_keyboard())

@bot.message_handler(func=lambda m: m.text == 'индивидульный курс')
def handle_individual_course(message):
    individual.handle(bot, message)

@bot.message_handler(func=lambda m: m.text == 'подарить сертификат')
def handle_gift_course(message):
    gift.handle(bot, message)

@bot.message_handler(func=lambda m: m.text == 'интенсив')
def handle_intense_course(message):
    intense.handle(bot, message)

@bot.message_handler(func=lambda m: m.text == 'мероприятие')
def handle_event_course(message):
    event.handle(bot, message)

@bot.message_handler(func=lambda m: m.text == 'коворкинг')
def handle_kovorking_course(message):
    kovorking.handle(bot, message)

@bot.message_handler(func=lambda m: m.text == 'свидание')
def handle_meeting_course(message):
    meeting.handle(bot, message)

def run_bot():
    print("Бот запущен")
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(debug=True, use_reloader=False)
