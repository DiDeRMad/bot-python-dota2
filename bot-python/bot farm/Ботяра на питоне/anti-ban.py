import requests
import time

VPN_API_KEY = "YOUR_VPN_SERVICE_API_KEY"  # API-ключ от VPN

def change_ip():
    """Запрос на смену IP через VPN API"""
    try:
        response = requests.get(f"https://vpn-provider.com/api/change-ip?key={VPN_API_KEY}") #тут крч можно просто добавить через outline самое простое ну или вдску оформлять на бота
        if response.status_code == 200:
            print("[INFO] IP успешно сменён")
        else:
            print("[ERROR] Не удалось сменить IP")
    except Exception as e:
        print(f"[ERROR] Ошибка смены IP: {e}")

if name == "main":
    while True:
        change_ip()
        time.sleep(1800)  # хз захотел чтобы меняло каждые 30 мин