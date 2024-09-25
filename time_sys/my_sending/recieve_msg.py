"""
This file is dedicated to checking the messages sent by different users.
These messages will update the users file.
"""

import requests


def check_incoming_msg() -> list[dict] | None:
    """
    check_incoming_msg checks for messages sent by users.
    The messages are found in the 'result' key given when
    a URL is called.

    received : {'ok' : True, 'result' : [...]}
    """
    TOKEN = '7273426065:AAFXQWFSzHhuUNyAEv9DKSuCPdiBJlF85qU'
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    received = requests.get(url).json()
    if received['result']:
        print(f'check_incoming_msg | Received : {received["result"]}')
        return received['result']
    else:
        print('check_incoming_msg | No new messages!')

