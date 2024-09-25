"""
This file contains code relating to
storing data relative to the program.
"""

import json


def store_stocks(stock_file, stock_dict : dict) -> None:
    """
    store_stocks stores the prices of the stock relative to its symbol.

    stock_file : Path(folder/to/file)
    stock_dict : {'symbol' : price}
    """
    with open(stock_file) as file:
        current_data = json.load(file)
    for symbol, price in stock_dict.items():
        current_data[symbol] = price
    with open(stock_file, 'w') as file:
        json.dump(current_data, file)


def store_users(user_file, user_dict : dict) -> None:
    """
    store_users stores the chat ID, name, and stocks related to the user.
    Returns None.

    user_file : Path(folder/to/file)
    user_dict : {'chat id' : ['name', [stocks]]}
    """
    with open(user_file) as file:
        current_data = json.load(file)
    for chat_id, tuple_list in user_dict.items():
        current_data[chat_id] = tuple_list
    with open(user_file, 'w') as file:
        json.dump(current_data, file)
