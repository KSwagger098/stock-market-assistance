"""
This file is dedicated to checking the messages sent by different users.
These messages will update the users file.
"""

import requests

TOKEN = '7273426065:AAFXQWFSzHhuUNyAEv9DKSuCPdiBJlF85qU'


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
        print(f'\ncheck_incoming_msg | Received : {received["result"]} | {received["result"][-1]["update_id"]} ~ {type(received["result"][-1]["update_id"])}')
        return received['result']
    else:
        print('\ncheck_incoming_msg | No new messages!')


def clear_msg(most_recent_msg: int) -> None:
    """
    Takes the update id of a user's message and takes their message out of the incoming message cue
    """
    offset_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={most_recent_msg + 1}"
    requests.get(offset_url)
