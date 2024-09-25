"""
This file is where time is controlled
and where most of the program will run.
"""

import datetime, json, time
from pathlib import Path
from my_sending import send_msg, format_msg, recieve_msg
from gathering import stock_price, symbol_existance
from storing import store_data, sort_users
from commanding import run_command


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
        time.sleep(2)
        if minute_time == '30' and current_time not in list(time_dict.keys()) and {13 > int(current_time[0:2]) > 5}:
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
    print(f'\nmessage_update | {bool(messages)}\n')
    if messages:
        with open(USER_PATH) as file:
            user_dict = json.load(file)
        sorted_user_dict, user_commands_list_tuple = sort_users.sort_users(user_dict, messages)
        print(f'AFTER-IF | sorted_user_dict {sorted_user_dict} | user_commands {user_commands_list_tuple}\n')
        store_data.store_users(USER_PATH, sorted_user_dict)
        for tuple_command in user_commands_list_tuple:
            with open(USER_PATH) as file:
                user_dict : dict = json.load(file)
            user_dict, msg = run_command.run_commands(user_dict, stock_price.scrap_yahoo, symbol_existance.stock_exists, tuple_command[1], tuple_command[0])
            with open(USER_PATH, 'w') as file:
                json.dump(user_dict, file)
            send_msg.send(msg, tuple_command[0])
            recieve_msg.clear_msg(tuple_command[2])


# update_data(['JPM', 'SAFE', 'AAPL'])
