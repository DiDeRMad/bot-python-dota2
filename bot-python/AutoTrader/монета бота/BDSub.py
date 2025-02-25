import sqlite3

# Создаем базу данных пользователей
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, premium INTEGER)")
conn.commit()

def check_premium(user_id):
    """ Проверяет, есть ли у пользователя подписка """
    cursor.execute("SELECT premium FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result and result[0] == 1

def activate_premium(user_id):
    """ Активирует премиум-доступ """
    cursor.execute("INSERT INTO users (user_id, premium) VALUES (?, ?)", (user_id, 1))
    conn.commit()

# Проверяем подписку перед запуском бота
user_id = 12345
if check_premium(user_id):
    print("✅ У вас премиум-доступ")
else:
    print("❌ У вас нет подписки")