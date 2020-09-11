from twilio.rest import Client


def connect(account, token):
    account_sid = account
    auth_token = token
    return Client(account_sid, auth_token)


def run(account, token, source, phone, url):
    call = connect(account=account, token=token).calls.create(
        url='{}'.format(url),
        from_='{}'.format(source),
        to='{}'.format(phone)
    )
    return call
