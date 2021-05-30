from twilio.rest import Client
def save(phone, code):

    account_sid = 'ACf0bad89842445357aa2626d4968c0e70'
    auth_token = '09ec5f919f0e75a905f0c0c33827668f'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+16183396762',
        body="Проверечный код: " + str(code) + " не отправляйте этот код никому",
        to=phone
        )
    print(message.sid)