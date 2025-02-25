import telebot
import subprocess

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Отправь /run для запуска бота или /stop для остановки.")

@bot.message_handler(commands=['run'])
def run_bot(message):
    bot.reply_to(message, "Запускаю Dota 2 бота...")
    subprocess.Popen(["python", "dota_bot.py"])  # Запуск скрипта бота

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    bot.reply_to(message, "Останавливаю бота...")
    subprocess.call(["pkill", "-f", "dota_bot.py"])  # Остановка процесса

if name == "main":
    bot.polling()