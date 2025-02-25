import requests

PUBLIC_ID = "ТВОЙ_PUBLIC_ID"
API_SECRET_KEY = "ТВОЙ_SECRET_KEY"

def check_payment(transaction_id):
    """ Проверяет статус платежа """
    url = "https://api.cloudpayments.ru/payments/get"
    auth = (PUBLIC_ID, API_SECRET_KEY)
    data = {"TransactionId": transaction_id}

    response = requests.post(url, auth=auth, json=data)
    result = response.json()

    if result.get("Success") and result["Model"]["Status"] == "Completed":
        return True  # Оплата прошла
    return False  # Оплаты нет

def create_payment(amount, email, user_id):
    """ Создает ссылку на оплату """
    url = "https://api.cloudpayments.ru/payments/cards/charge"
    auth = (PUBLIC_ID, API_SECRET_KEY)
    data = {
        "Amount": amount,
        "Currency": "RUB",
        "IpAddress": "192.168.1.1",
        "Description": "Подписка на бота",
        "AccountId": user_id,  # ID пользователя
        "Email": email,
        "CardCryptogramPacket": "CRYPT_DATA"
    }

    response = requests.post(url, auth=auth, json=data)
    return response.json()

# Пример: создаем платеж на 500 руб.
payment = create_payment(500, "user@example.com", "12345")
print(payment)