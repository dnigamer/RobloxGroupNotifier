from twilio.rest import Client


def connect(account, token):
    account_sid = account
    auth_token = token
    return Client(account_sid, auth_token)


def run(account, token, profile, message, date, source, phone):
    message = connect(account=account, token=token).messages.create(
        body="{} said {} at {}".format(profile, message, date),
        from_='{}'.format(source),
        to='{}'.format(phone)
    )
    return message
