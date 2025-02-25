def sell_item(item_id, sell_price):
    """ Выставляет предмет на продажу """
    user = login_steam()
    if not user:
        return
    
    sell_url = "https://steamcommunity.com/market/sellitem/"
    payload = {
        "sessionid": user.session_id,
        "appid": 570,  # Dota 2
        "contextid": 2,
        "assetid": item_id,
        "price": int(sell_price * 100),
        "currency": 5
    }
    
    response = user.session.post(sell_url, data=payload)
    if response.status_code == 200:
        print(f"Предмет {item_id} выставлен за {sell_price} руб.")
    else:
        print("Ошибка при продаже:", response.text)

# Пример продажи предмета
sell_item("1234567890", 1500)  # ID предмета и цена