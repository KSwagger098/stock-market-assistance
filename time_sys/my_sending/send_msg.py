"""
This is where the sending functionality is programmed.
"""

import requests
from pathlib import Path


def send(msg : str, chat_id : str) -> None:
    """
    Sends any string message to the user.
    """
    token_path = Path.cwd() / 'time_sys' / 'api-codes' / 'telergam-api.txt'
    with open(token_path) as token_file:
        TOKEN : str = token_file.read()
    print(f'send | Using {TOKEN}')
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}'
    info = requests.get(url).json()
    print(f"SEND FUNCTION | info : {info['result']['text']}\n")

