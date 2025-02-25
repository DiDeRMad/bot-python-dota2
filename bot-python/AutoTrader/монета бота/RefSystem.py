# Добавляем рефералов в базу
cursor.execute("CREATE TABLE IF NOT EXISTS referrals (referrer_id INTEGER, referred_id INTEGER)")
conn.commit()

def add_referral(referrer_id, referred_id):
    """ Записывает реферала в базу данных """
    cursor.execute("INSERT INTO referrals (referrer_id, referred_id) VALUES (?, ?)", (referrer_id, referred_id))
    conn.commit()

def count_referrals(referrer_id):
    """ Считает количество рефералов у пользователя """
    cursor.execute("SELECT COUNT(*) FROM referrals WHERE referrer_id = ?", (referrer_id,))
    return cursor.fetchone()[0]

# Пример: пользователь 12345 пригласил 67890
add_referral(12345, 67890)

# Проверяем, сколько людей пригласил 12345
print(f"У пользователя 12345 {count_referrals(12345)} рефералов")