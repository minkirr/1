from flask import Flask, request, jsonify
import json
import threading
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import individual, gift, intense, event, kovorking, meeting
import individual
import requests

API_TOKEN = '7561870576:AAHSEpjx1nNH4aa6WBwNEe3MQzmWSsKUOCA'  # Замените на свой токен
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
    bot.send_message(message.chat.id, "Я бот лобзика бла бла помогу выбрать бла бла что вас интересует?", reply_markup=create_main_keyboard())

@bot.message_handler(content_types=['web_app_data'])
def web_app(message: types.Message):
    try:
        # Получаем данные из WebApp
        data = json.loads(message.web_app_data.data)

        # Логируем данные, чтобы убедиться, что они приходят
        print(f"Полученные данные: {data}")

        # Отправляем данные на сервер Flask
        response = requests.post("http://127.0.0.1:5000/webapp_data", json=data)
        if response.status_code == 200:
            print("Данные успешно отправлены на сервер.")
            bot.send_message(
                message.chat.id,
                f"Получены данные:\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nДанные успешно сохранены!"
            )
        else:
            print("Ошибка при отправке данных на сервер.")
            bot.send_message(message.chat.id, "Произошла ошибка при отправке данных на сервер.")
        
    except Exception as e:
        # Если возникла ошибка, выводим её в консоль
        print(f"Ошибка при обработке данных: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке данных.")





@bot.message_handler(func=lambda m: m.text == 'Индивидуальный курс')
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
