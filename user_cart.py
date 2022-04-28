import items


def populate_user_cart(user_cart, item):
    user_cart.append(item)
    return user_cart


def cart_creation():
    user_cart = []
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic hat a", 5.99, "clothing"))
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic hat b", 9.99, "clothing"))
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic food a", 1.00, "wic eligible food"))
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic food b", 3.00, "wic eligible food"))
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic item a", 10.99, "everything else"))
    user_cart = populate_user_cart(user_cart, items.InventoryItem("generic item b", 15.99, "everything else"))
    return user_cart
