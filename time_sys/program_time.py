"""
This file is where time is controlled
and where most of the program will run.
"""

import datetime, json, time
from pathlib import Path
from my_sending import send_msg, format_msg, recieve_msg
from gathering import stock_price
from storing import store_data, sort_users


STOCK_PATH = Path.cwd()/'time_sys'/'storing'/'stocks.json'
USER_PATH = Path.cwd()/'time_sys'/'storing'/'users.json'


def start() -> None:
    """
    This function begins the program and runs the program until 12:30. Returns None.
    """
    time_dict = {}
    while True:
        print(f'Current Saved Times: {time_dict}')
        print_time = str(datetime.datetime.now().time())[0:8]
        current_time = print_time[0:5]
        minute_time = current_time[3:5]
        print(f'Current Time : {current_time} | Minute Time : {minute_time} ~ Type: {type(minute_time)} | print time : {print_time}')
        print(f'{minute_time == "30"} | {current_time not in list(time_dict.keys())} | {13 > int(current_time[0:2]) > 5}')
        time.sleep(5)
        if minute_time == '30' and current_time not in list(time_dict.keys()):
            time_dict[current_time] = True
            print("WENT THROUGH!")
            with open(USER_PATH) as file:
                user_information: dict = json.load(file)
            with open(STOCK_PATH) as file:
                old_stock_price: dict = json.load(file)
            for chat_id, user_tuple in user_information.items():
                new_stock_price: dict = stock_price.scrap_yahoo(user_tuple[1])
                msg: str = format_msg.format_update_msg(current_time, new_stock_price, old_stock_price, user_tuple[0])
                send_msg.send(msg, chat_id)
            store_data.store_stocks(STOCK_PATH, new_stock_price)
        message_update()


def update_stock_data(stock_list : list) -> None:
    """
    update_stock_data updates the stock data with the most current data.
    """
    stock_dict : dict = stock_price.scrap_yahoo(stock_list)
    store_data.store_stocks(STOCK_PATH, stock_dict)


def message_update() -> None:
    """
    This function is called every second since the incoming messages need to be checked every few seconds.
    """
    messages = recieve_msg.check_incoming_msg()
    if messages:
        with open(USER_PATH) as file:
            user_dict = json.load(file)
        sorted_user_dict, user_commands_list_tuple = sort_users.sort_users(user_dict, messages)
        store_data.store_users(USER_PATH, sorted_user_dict)


# update_data(['JPM', 'SAFE', 'AAPL'])
if __name__ == "__main__":
    start()
