import re


def get_users_state():
    runner = -1
    state = 0
    while runner == -1:
        state = (input("Please enter 1 if you are in MA, 2 if in NH, or 3 if you are in ME"))
        if handle_user_state(state) == 0:
            runner = 0
        else:
            print("Please enter the correct number")
    return int(state)


def handle_user_state(state):
    if type(state) == str:
        match = re.match("[1-3]", state)
        is_match = bool(match)
        if is_match:
            if len(state) == 1:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 1


def get_total_ma(list_of_items):
    total = 0
    for i in range(len(list_of_items)):
        if list_of_items[i].item_type == "everything else":
            total = total + list_of_items[i].item_price + (list_of_items[i].item_price * 0.0625)
        else:
            total = total + list_of_items[i].item_price
    return total


def get_total_nh(list_of_items):
    total = 0
    for i in range(len(list_of_items)):
        total = total + list_of_items[i].item_price
    return total


def get_total_me(list_of_items):
    total = 0
    for i in range(len(list_of_items)):
        if list_of_items[i].item_type == "wic eligible food":
            total = total + list_of_items[i].item_price
        else:
            total = total + list_of_items[i].item_price + (list_of_items[i].item_price * 0.055)
    return total
