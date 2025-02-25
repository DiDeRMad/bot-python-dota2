import pymem
import pymem.process

def get_dota_memory():
    """Получает доступ к процессу Dota 2"""
    try:
        pm = pymem.Pymem("dota2.exe")
        return pm
    except Exception as e:
        print(f"[ERROR] Не удалось получить доступ к процессу: {e}")
        return None

def read_health(pm, address):
    """Чтение значения здоровья"""
    try:
        health = pm.read_int(address)
        return health
    except:
        return None

def read_mana(pm, address):
    """Чтение значения маны"""
    try:
        mana = pm.read_int(address)
        return mana
    except:
        return None

if name == "main":
    pm = get_dota_memory()
    if pm:
        health_address = 0x12345678  # тут крч потом посидеть и найти адрес через чит энжин
        mana_address = 0x87654321  # тут крч потом посидеть и найти адрес через чит энжин

        while True:
            hp = read_health(pm, health_address)
            mp = read_mana(pm, mana_address)
            print(f"[INFO] Здоровье: {hp}, Мана: {mp}")