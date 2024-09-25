"""
This part of the program checks if a certain stock exists.
"""

import finnhub
import finnhub.client

API_KEY = 'crmk5p9r01qhaloduv80crmk5p9r01qhaloduv8g'


def current_price(stock_list : list) -> dict[str : int]:
    """
    This function gets the current prices of a given list of stocks.
    Returns a dictionary of stocks with it's current price.
    """
    return_dict = {}
    finnhub_client = finnhub.Client(api_key=API_KEY)
    for stock in stock_list:
        return_dict[stock] = finnhub_client.get
