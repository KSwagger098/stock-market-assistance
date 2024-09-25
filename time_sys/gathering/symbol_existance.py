"""
This part of the program checks if a certain stock exists.
"""

import finnhub
import finnhub.client
from pathlib import Path


def stock_exists(stock: str, type_of_call: str = None) -> bool:
    """
    This function gets the current prices of a given list of stocks.
    Returns a dictionary of stocks with it's current price.
    """
    api_key_path : str = Path.cwd() / 'time_sys' / 'api-codes' / 'finnhub-api.txt'
    with open(api_key_path) as key_file:
        API_KEY : str = key_file.read()
    print(f'stock_exists | Using {API_KEY}')
    finnhub_client = finnhub.Client(api_key=API_KEY)
    outcome = finnhub_client.symbol_lookup(stock)
    print(outcome)
    if not type_of_call:
        return bool(outcome["count"])
    elif type_of_call == '!add':
        for stock_dict in outcome["result"]:
            if stock_dict['displaySymbol'] == stock:
                return True
        return False


# Testing
# print(f"Testing | {stock_exists('POOP', '!add')}")
