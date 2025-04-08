#API_TOKEN = '7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ'
#https://strangepineaplle.github.io/lobzik-web/

from flask import Flask, jsonify, request
import json
import telebot
import individual

TOKEN = "7973114067:AAGM3sHdKjGOIurgmJaIT041Df3dc5QaCGQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
DATA_FILE = "data.json"

@app.route("/free_slots", methods=["GET"])
def get_free_slots():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        slots = json.load(file)
    free = [s for s in slots if s["тип"] == "индивидульный курс" and s["фио"] == ""]
    return jsonify(free)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        slots = json.load(file)

    for slot in slots:
        if slot["дата"] == data["дата"] and slot["время"] == data["время"] and slot["фио"] == "":
            slot["фио"] = data["фио"]
            slot["телефон"] = data["телефон"]
            slot["оплата"] = "ожидает оплаты"
            slot["tg_id"] = data["tg_id"]
            break
    else:
        return "Слот уже занят или не найден", 400

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(slots, file, ensure_ascii=False, indent=2)

    return "Данные успешно отправлены!"

# Обработка команды через индивидуальный файл
@bot.message_handler(func=lambda m: m.text == "🧑‍🏫 Индивидуальный курс")
def handle_individual(message):
    individual.handle(bot, message)

if __name__ == "__main__":
    print("Бот запущен")
    import threading
    threading.Thread(target=bot.polling, daemon=True).start()
    app.run(debug=True)
