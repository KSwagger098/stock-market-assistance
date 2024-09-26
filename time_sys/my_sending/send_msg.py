"""
This is where the sending functionality is programmed.
"""

import requests
from pathlib import Path


def send(msg : str, chat_id : str, fetch_token_function) -> None:
    """
    Sends any string message to the user.
    """
    TOKEN = fetch_token_function("telegram_bot_token")
    print(f'send | Using {TOKEN}')
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}'
    info = requests.get(url).json()
    print(f"raw-info : {info}")
    print(f"SEND FUNCTION | info : {info['result']['text']}\n")

