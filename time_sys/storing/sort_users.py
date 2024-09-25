"""
sort_users.py sorts the users and their commands into a dictionary given a message.
{'chat id' : ['name', [stock]]}
"""

# 'result': [
#               {'update_id': 120419344,
#                'message': {'message_id': 3,
#                            'from': {'id': 5295637164,
#                                     'is_bot': False,
#                                     'first_name': 'Otaku',
#                                     'last_name': 'Versus',
#                                     'username': 'Miyage4444',
#                                     'language_code': 'en'},
#                                     'chat': {'id': 5295637164,
#                                              'first_name': 'Otaku',
#                                              'last_name': 'Versus',
#                                              'username': 'Miyage4444',
#                                              'type': 'private'},
#                                              'date': 1725936532,
#                                              'text': 'Test tea'}}]}

def sort_users(user_dict, received_msgs : list[dict]) -> tuple[dict, list]:
    """
    sort_users takes the received messages and filters out the important information needed.
    Returns a tuple containing the dictionary for the data and a list-tuple for possible commands.

    user_dictionary : {'chat id' : ['name', [stock]]}
    command_list_tuple   : [('chat id', 'command')]
    """
    command_list_tuple = []
    for msg_dict in received_msgs:
        chat_id = str(msg_dict['message']['from']['id'])
        command_list_tuple.append((chat_id, msg_dict['message']['text'], msg_dict["update_id"]))
        if chat_id not in list(user_dict.keys()):
            first_name = msg_dict['message']['from']['first_name']
            user_dict[chat_id] = [first_name, []]
    return user_dict, command_list_tuple
