import requests

TELEGRAM_BOT_TOKEN = "БОТ_ТОКЕН"
TELEGRAM_CHAT_ID = "CHAT_ID"

def send_telegram_message(text):
    """ Отправляет сообщение в Telegram """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    requests.post(url, json=payload)

# Пример: уведомление о сделке
send_telegram_message("✅ Бот купил предмет за 500 руб, продал за 700 руб (+200 руб профита)")