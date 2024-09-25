"""
This module deals with running commands.
"""

from pathlib import Path

COMMAND_MSG_PATH = Path().cwd()/'time_sys'/'commanding'/'commands_msg.txt'

def run_commands(user_dict: dict, yahoo_scrap, check_symbol, command: str, chat_id: str) -> tuple[dict, str]:
    """
    Takes a command and returns a message to the user and an update user dictionary.

    tuple_command_ : ('chat_id', 'command')
    user_dict : {'chat_id' : ['first_name', [stocks]]}
    """
    split_commands = command.split(' ')
    if split_commands[0] == '!commands' and len(split_commands) == 1:
        with open(COMMAND_MSG_PATH) as message:
            msg = message.read()
    elif split_commands[0] == '!add' and len(split_commands) == 2:
        if check_symbol(split_commands[1]):
            user_dict[chat_id][1].append(str(split_commands[1]).upper())
            msg = f'{str(split_commands[1]).upper()} has been added to your list of stock!'
        else:
            msg = f'{split_commands[1]} does not exist!'
    elif split_commands[0] == '!remove' and len(split_commands) == 2:
        if str(split_commands[1]).upper() in user_dict[chat_id][1]:
            user_dict[chat_id][1].remove(str(split_commands[1]).upper())
            msg = f'{str(split_commands[1]).upper()} has been removed from your list of stock!'
        else:
            msg = f'{split_commands[1]} cannot be removed since it\'s not present in your list of stocks.\nPlease refer to !stock to check your list of stocks.'
    elif split_commands[0] == '!stock' and len(split_commands) == 1:
        msg = 'Here is your stock list:\n'
        stock_list_int = 1
        for stock in user_dict[chat_id][1]:
            msg += f'{stock_list_int}. {stock} | ${yahoo_scrap([stock])[stock]}\n'
            stock_list_int += 1
    else:
        msg = 'Please use the \'!commands\' command to refer to the list of commands.'
    return user_dict, msg
