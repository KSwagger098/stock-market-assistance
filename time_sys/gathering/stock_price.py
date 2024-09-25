"""
This part of the program gets data
on the current prices of stocks via web-scrapping
"""

import requests
from bs4 import BeautifulSoup


def scrap_yahoo(stock_list : list) -> dict[str : int]:
    """
    Scrapping from Yahoo Finance, gets the price of a stock and returns a dictionary.

    return_dict : {'symbol' : price}
    """
    return_dict = {}
    for stock in stock_list:
        request_yahoo = requests.get(f'https://finance.yahoo.com/quote/{stock}/')
        # print(request_yahoo)  # Response 200 means success!

        html_data = BeautifulSoup(request_yahoo.content, 'html.parser')
        # print(html_data.prettify())
        price = html_data.find('fin-streamer', class_ = 'livePrice yf-1i5aalm').text
        return_dict[stock] = price
    return return_dict

