from twilio.rest import Client
def save(phone, code):

    account_sid = 'ACed56d9ea62b2b6e9b0a1e5adbee0b492'
    auth_token = '88e35009e2e9643618804b9d62efd126'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='(361) 245-5404',
        body="Проверечный код: " + str(code) + " не отправляйте этот код никому",
        to=phone
        )
    print(message.sid)