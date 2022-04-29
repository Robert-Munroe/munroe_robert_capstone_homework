import pytest
import items
import main


def test_production_function_type():
    cart = [(items.InventoryItem("generic hat a", 5.99, "clothing"))]
    total = main.calculate_for_state(1, cart)
    assert type(total) is float
    assert total == 5.99


def test_production_function_tax_rate_ma():
    cart = [(items.InventoryItem("generic item c", 100, "everything else"))]
    total = main.calculate_for_state(1, cart)
    total_tax = total - cart[0].item_price
    assert total_tax == 6.25


def test_production_function_tax_rate_me():
    cart = [(items.InventoryItem("generic item c", 100, "everything else"))]
    total = main.calculate_for_state(3, cart)
    total_tax = total - cart[0].item_price
    assert total_tax == 5.5


def test_production_function_tax_rate_me_clothes():
    cart = [(items.InventoryItem("generic item c", 100, "clothing"))]
    total = main.calculate_for_state(3, cart)
    total_tax = total - cart[0].item_price
    assert total_tax == 5.5


def test_production_function_empty_cart():
    cart = []
    total = main.calculate_for_state(1, cart)
    assert total == 0
