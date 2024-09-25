"""
This is where the sending functionality is programmed.
"""

import requests


def send(msg : str, chat_id : str) -> None:
    """
    Sends any string message to the user.
    """
    TOKEN = '7273426065:AAFXQWFSzHhuUNyAEv9DKSuCPdiBJlF85qU'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}'
    info = requests.get(url).json()
    print(f"SEND FUNCTION | info : {info['result']['text']}")

