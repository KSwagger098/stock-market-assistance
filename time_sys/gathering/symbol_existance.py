"""
This part of the program checks if a certain stock exists.
"""

import finnhub
import finnhub.client

API_KEY = 'crmk5p9r01qhaloduv80crmk5p9r01qhaloduv8g'


def stock_exists(stock: str) -> bool:
    """
    This function gets the current prices of a given list of stocks.
    Returns a dictionary of stocks with it's current price.
    """
    finnhub_client = finnhub.Client(api_key=API_KEY)
    outcome = finnhub_client.symbol_lookup(stock)
    return bool(outcome["count"])
