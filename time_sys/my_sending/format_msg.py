"""
This file is used to format
messages that will be sent
to the user.
"""

def format_update_msg(current_time: str, new_stock_data: dict, old_stock_data: dict, first_name: str) -> str:
    """
    Formats a message that shows if the stock has gone up or down.
    Returns a string that will be sent to the user.

    stock_data : {'symbol' : price}
    """
    msg = ''
    if current_time == '06:30':
        msg += f"Good Morning, {first_name}\n\nHere is your first report for today!\n\n"
    elif current_time == '12:30':
        msg += f"Good Evening, {first_name}\n\nHere is your last report for today!\n\n"
    else:
        msg += f"{first_name}! Your hourly report on your chosen stocks are here!\n\n"
    stock_list_int = 1
    for stock, price in new_stock_data.items():
        old_stock_price = round(float(old_stock_data[stock]), 2)
        new_stock_price = round(float(new_stock_data[stock]), 2)
        msg += f"{stock_list_int}. {stock} | {price} | {'New Stock!' if stock not in list(old_stock_data.keys()) else f'DOWN {round(old_stock_price - new_stock_price, 2)}' if old_stock_price > new_stock_price else f'UP {round(new_stock_price - old_stock_price, 2)}' if old_stock_price < new_stock_price else 'NO CHANGE'}\n\n"
        stock_list_int += 1
    if current_time != '12:30' and int(current_time[0:2]) > 10:
        msg += f"I will update you at 0{int(current_time[0:2])}:30 for your hourly stock report!"
    elif current_time != '12:30' and int(current_time[0:2]) > 10:
        msg += f"I will update you at {int(current_time[0:2])}:30 for your hourly stock report!"
    else:
        msg += f"I will update you tommorow at 06:30 for your next hourly report tommorow! Have a great rest of your day!"
    return msg
