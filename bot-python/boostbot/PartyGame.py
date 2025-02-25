import requests

SERVER_URL = "http://localhost:5000"

def send_command_to_teammates(command):
    """Отправляет команду ботам-тиммейтам"""
    requests.post(f"{SERVER_URL}/command", json={"cmd": command})

# Пример: отправляем команде команду на драку
send_command_to_teammates("attack_mid")