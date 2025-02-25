import time

ITEMS_TO_TRACK = {
    "Treasure of the Crimson Witness 2018": {"buy_price": 900, "sell_price": 1200},
    "Golden Basher Blades": {"buy_price": 2000, "sell_price": 2500},
}

def main():
    while True:
        for item, price_limits in ITEMS_TO_TRACK.items():
            price = get_item_price(item)
            if price:
                print(f"{item}: {price} руб.")
                if price <= price_limits["buy_price"]:
                    buy_item(item, price_limits["buy_price"])
                elif price >= price_limits["sell_price"]:
                    print(f"Цена на {item} высокая, можно продавать!")
        time.sleep(60)  # Обновлять каждые 60 секунд

# Запуск мониторинга
main()