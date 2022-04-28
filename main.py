# Robert Munroe
# Homework

import user_cart
import calculations


def calculate_for_state(state, customer_cart):
    if state == 1:
        total = calculations.get_total_ma(customer_cart)
        return round(total, 2)
    if state == 2:
        total = calculations.get_total_nh(customer_cart)
        return round(total, 2)
    if state == 3:
        total = calculations.get_total_me(customer_cart)
        return round(total, 2)


def main():
    customer_cart = user_cart.cart_creation()
    state = calculations.get_users_state()
    total = calculate_for_state(state, customer_cart)
    print(f"Your total is:  ${total}")


if __name__ == '__main__':
    main()
