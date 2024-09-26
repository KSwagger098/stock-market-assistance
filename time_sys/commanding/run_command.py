"""
This module deals with running commands.
"""

from pathlib import Path


def run_commands(user_dict: dict, yahoo_scrap, check_symbol, send_function, fetch_token_function, command: str, chat_id: str) -> tuple[dict, str]:
    """
    Takes a command and returns a message to the user and an update user dictionary.

    tuple_command_ : ('chat_id', 'command')
    user_dict : {'chat_id' : ['first_name', [stocks]]}
    """
    split_commands = command.split(' ')
    if split_commands[0] == '!commands' and len(split_commands) == 1:
        msg = command_function()
    elif split_commands[0] == '!add':
        user_dict, msg = add_function(split_commands, check_symbol, send_function, fetch_token_function, user_dict, chat_id)
    elif split_commands[0] == '!remove':
        user_dict, msg = remove_function(split_commands, send_function, fetch_token_function, user_dict, chat_id)
    elif split_commands[0] == '!stock' and len(split_commands) == 1:
        msg = 'Here is your stock list:\n'
        stock_list_int = 1
        if user_dict[chat_id][1]:
            for stock in user_dict[chat_id][1]:
                msg += f'{stock_list_int}. {stock} | ${yahoo_scrap([stock])[stock]}\n'
                stock_list_int += 1
        else:
            msg += '\n Wow... Such Empty...\n\nPlease use \'!add\' command to add a stock!'
    else:
        msg = 'Please use the \'!commands\' command to refer to the list of commands.'
    return user_dict, msg


def command_function() -> str:
    """
    Returns the command list found in comamnds_msg.txt
    """
    COMMAND_MSG_PATH = Path().cwd()/'time_sys'/'commanding'/'commands_msg.txt'
    with open(COMMAND_MSG_PATH) as message:
        msg = message.read()
    return msg


def add_function(split_commands : list[str], check_symbol, send_function, fetch_token_function, user_dict : dict, chat_id : str) -> tuple[dict, str]:
    """
    Takes the user's message, checks if given stock(s) exists, and sends the messages to the user within the function.
    Returns an updated user_dict and an empty string.

    split_commands : ['!add', 'JPM', 'AAPL', ...]
    check_symbol : function (symbol_existance.stock_exists(stock : str))
    send_function : function (send_msg.send(msg : str, chat_id : str))
    fetch_token_function : function (return_tokens.give_token(variable_name: str))
    user_dict : {'chat_id' : ['first_name', [stocks]]}
    chat_id : personalized string used to send messages to certain users
    """
    if len(split_commands) > 1:
        for stock_symbol in split_commands[1:]:
            if stock_symbol == ',':
                pass
            elif stock_symbol[-1] == ',':
                stock_symbol = stock_symbol[:len(stock_symbol) - 1]
            if check_symbol(str(stock_symbol).upper(), fetch_token_function("FINNHUB_TOKEN"), '!add'):
                user_dict[chat_id][1].append(str(stock_symbol).upper())
                send_function(f'{str(stock_symbol).upper()} has been added to your list of stock!', chat_id, fetch_token_function)
            else:
                send_function(f'{stock_symbol} does not exist!', chat_id, fetch_token_function)
    else:
        msg = f'To use the \'!add\' function, simply type:\n\'!add [the stocks you want to add]\'.\n\nFor example:\n\'!add JPM AAPL MSFT\'\n\nIt doesn\'t have to be a list, just add the stock symbol(s) after the command!'
        send_function(msg, chat_id, fetch_token_function)
    return user_dict, ''


def remove_function(split_commands : list[str], send_function, fetch_token_function, user_dict : dict, chat_id : str) -> tuple[dict, str]:
    """
    Takes the user's message and checks what stocks they would like to remove from their list of stocks.
    Returns a dictionary of their updated list and an empty string.

    split_commands : ['!remove', 'JPM', 'AAPL', ...]
    send_function : function (send_msg.send(msg : str, chat_id : str))
    user_dict : {'chat_id' : ['first_name', [stocks]]}
    chat_id : personalized string used to send messages to certain users
    """
    if len(split_commands) > 1:
        for stock in split_commands[1:]:
            if str(stock).upper() in user_dict[chat_id][1]:
                user_dict[chat_id][1].remove(str(stock).upper())
                send_function(f'{str(stock).upper()} has been removed from your list of stock!', chat_id, fetch_token_function)
            else:
                send_function(f'{stock} cannot be removed since it\'s not present in your list of stocks.\nPlease refer to !stock to check your list of stocks.', chat_id, fetch_token_function)
    else:
        msg = f'To use the \'!remove\' function, simply type:\n\'!remove [the stocks you want to remove]\'.\n\nFor example:\n\'!remove JPM AAPL MSFT\'\n\nIt doesn\'t have to be a list, just add the stock symbol(s) after the command!'
        send_function(msg, chat_id, fetch_token_function)
    return user_dict, ''
