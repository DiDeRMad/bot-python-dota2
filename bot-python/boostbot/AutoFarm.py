import keyboard

def attack_creeps():
    """Атакует крипов, если видит их в поле зрения"""
    while True:
        creep = pyautogui.locateCenterOnScreen('creep.png', confidence=0.8)
        if creep:
            pyautogui.moveTo(creep)
            pyautogui.click()
            print("[+] Атакуем крипа")
        time.sleep(0.5)

# Запуск фарма крипов
attack_creeps()