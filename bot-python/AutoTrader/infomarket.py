import steam.webauth as wa
import requests

STEAM_USERNAME = "your_steam_username"
STEAM_PASSWORD = "your_steam_password"

def login_steam():
    """ Авторизация в Steam """
    session = wa.WebAuth(STEAM_USERNAME, STEAM_PASSWORD)
    try:
        user = session.cli_login()
        return user
    except wa.CaptchaRequired:
        print("Требуется капча")
        return None
    except wa.EmailCodeRequired:
        print("Требуется код с почты")
        return None
    except wa.TwoFactorCodeRequired:
        print("Требуется Steam Guard")
        return None

def buy_item(item_name, max_price):
    """ Покупает предмет, если цена ниже установленного лимита """
    price = get_item_price(item_name)
    
    if price and price <= max_price:
        user = login_steam()
        if user:
            buy_url = f"https://steamcommunity.com/market/buylisting/{item_name}"
            payload = {"sessionid": user.session_id, "currency": 5, "price_total": price * 100, "quantity": 1}
            headers = {"Referer": buy_url}
            response = user.session.post(buy_url, data=payload, headers=headers)

            if response.status_code == 200:
                print(f"Успешно куплен {item_name} за {price} руб.")
            else:
                print("Ошибка при покупке:", response.text)
        else:
            print("Ошибка авторизации")

# Пример покупки предмета
buy_item("Treasure of the Crimson Witness 2018", 1000)  # Лимит 1000 руб.