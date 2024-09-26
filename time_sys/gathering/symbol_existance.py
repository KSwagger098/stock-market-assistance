"""
This part of the program checks if a certain stock exists.
"""

import finnhub
import finnhub.client


def stock_exists(stock: str, API_KEY: str, type_of_call: str = None) -> bool:
    """
    This function gets the current prices of a given list of stocks.
    Returns a dictionary of stocks with it's current price.
    """
    print(f'stock_exists | Using {API_KEY}')
    finnhub_client = finnhub.Client(api_key=API_KEY)
    outcome = finnhub_client.symbol_lookup(stock)
    # print(outcome)
    if not type_of_call:
        return bool(outcome["count"])
    elif type_of_call == '!add':
        for stock_dict in outcome["result"]:
            if stock_dict['displaySymbol'] == stock:
                return True
        return False

