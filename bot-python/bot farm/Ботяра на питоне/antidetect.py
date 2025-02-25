import pydirectinput
import random
import time

def human_like_movement():
    """Имитация случайного движения мыши"""
    x, y = random.randint(100, 1800), random.randint(100, 900)
    duration = random.uniform(0.3, 1.2)  # Разные задержки
    pydirectinput.moveTo(x, y, duration=duration)
    print(f"[INFO] Движение в {x}, {y}")

def random_pause():
    """Случайные задержки, имитирующие поведение игрока"""
    delay = random.uniform(1.0, 5.0)
    print(f"[INFO] Ожидание {round(delay, 2)} сек...")
    time.sleep(delay)

if name == "main":
    while True:
        human_like_movement()
        random_pause()