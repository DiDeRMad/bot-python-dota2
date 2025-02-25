import pydirectinput
import pyautogui
import cv2
import numpy as np
import time
import random

# Настройки задержек и интервалов
MOVE_DELAY = 2
ATTACK_DELAY = 0.5
ITEM_USE_DELAY = 1
SHOP_DELAY = 2
SEARCH_INTERVAL = 0.5
ESCAPE_DELAY = 3

# Шаблоны изображений
TARGET_CREEP = "creep.png"  # Крип
ABILITY_ICON = "ability.png"  # Способность
HEAL_ITEM_ICON = "tango.png"  # Лечение (Tango, Salve)
MANA_ITEM_ICON = "clarity.png"  # Восстановление маны (Clarity, Mango)
SHOP_ICON = "shop.png"  # Магазин
ENEMY_ICON = "enemy.png"  # Враг на миникарте
HEALTH_BAR = "health_bar.png"  # Полоска здоровья
MANA_BAR = "mana_bar.png"  # Полоска маны

# Позиции безопасных зон (башни)
SAFE_ZONES = [(300, 300), (1600, 500), (900, 1000)]  # Башня на линии

# Заданные точки фарма
WAYPOINTS = [(500, 500), (1200, 900), (1600, 400), (800, 700)]


def find_target(target_img, threshold=0.8):
    """Поиск объекта на экране"""
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    template = cv2.imread(target_img, 0)
    w, h = template.shape[::-1]

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        x, y = loc[1][0], loc[0][0]
        return x + w // 2, y + h // 2
    return None


def move_to_waypoint():
    """Перемещение к точке фарма"""
    waypoint = random.choice(WAYPOINTS)
    pydirectinput.moveTo(waypoint[0], waypoint[1], duration=random.uniform(0.5, 1.5))
    pydirectinput.click()
    print(f"[INFO] Перемещение к фарму: {waypoint}")
    time.sleep(MOVE_DELAY)


def attack_creep():
    """Приоритетная атака крипов (добивание)"""
    coords = find_target(TARGET_CREEP)
    if coords:
        pydirectinput.moveTo(coords[0], coords[1])
        pydirectinput.click()
        print("[INFO] Атака крипа")
        time.sleep(ATTACK_DELAY)
        return True
    return False


def use_ability():
    """Использование способности (если доступна)"""
    coords = find_target(ABILITY_ICON)
    if coords:
        pydirectinput.press('q')  # Используем способность на 'Q'
        print("[INFO] Использование способности")
        time.sleep(ATTACK_DELAY)


def use_heal_item():
    """Использование лечения при низком HP"""
    health = find_target(HEALTH_BAR, threshold=0.6)
    if health:
        pydirectinput.press('3')  # Слот 3 (Tango, Salve)
        print("[INFO] Использование лечения")
        time.sleep(ITEM_USE_DELAY)


def use_mana_item():
    """Использование восстановления маны при низком уровне"""
    mana = find_target(MANA_BAR, threshold=0.6)
    if mana:
        pydirectinput.press('4')  # Слот 4 (Clarity, Mango)
        print("[INFO] Восстановление маны")
        time.sleep(ITEM_USE_DELAY)


def escape_to_safe_zone():
    """Сьёбываем в безопасную зону (если рядом враг)"""
    enemy = find_target(ENEMY_ICON, threshold=0.7)
    if enemy:
        safe_zone = random.choice(SAFE_ZONES)
        pydirectinput.moveTo(safe_zone[0], safe_zone[1], duration=1)
        pydirectinput.click()
        print("[WARNING] Враг найден! Сьёбываем в безопасную зону.")
        time.sleep(ESCAPE_DELAY)


def open_shop_and_buy():
    """Открытие магазина и покупка предметов"""
    gold = random.randint(1000, 3000)  # Примерное золото (в реальности читается из памяти)
    if gold >= 1500:  # Проверка минимальной суммы
        coords = find_target(SHOP_ICON)
        if coords:
            pydirectinput.press('b')  # Открыть магазин
            print("[INFO] Покупка предмета...")
            time.sleep(SHOP_DELAY)
            pydirectinput.click(x=1000, y=500)  # Предмет в магазине
            print("[INFO] Покупка выполнена")


def random_mouse_movement():
    """Рандомизация движений мыши (антидетект)"""
    x, y = random.randint(100, 1800), random.randint(100, 900)
    pydirectinput.moveTo(x, y, duration=random.uniform(0.2, 0.5))
    print("[INFO] Случайное движение мыши")
    def main_loop():
    """Основной цикл бота"""
    print("[INFO] Бот запущен...")
    while True:
        escape_to_safe_zone()  # Проверка на врагов
        move_to_waypoint()  # Фарм крипов
        attack_creep()  # Атака крипов
        use_ability()  # Использование способности
        use_heal_item()  # Лечение при низком HP
        use_mana_item()  # Восстановление маны
        open_shop_and_buy()  # Покупка предметов
        random_mouse_movement()  # Антидетект движения
        time.sleep(SEARCH_INTERVAL)


if name == "main":
    main_loop()