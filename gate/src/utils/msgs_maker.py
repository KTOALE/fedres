from json import dumps


def make_secret_msg(login=None, secret=None, secret_key=None, make_bytes=False):
    payload = dumps(
        {
            "secret": secret,
            "secret_phrase": secret_key,
            "email": login,
        }
    )
    return payload.encode() if make_bytes else payload
