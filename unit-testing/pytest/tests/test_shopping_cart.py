import pytest
from app.shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    cart.add_item("banana", 4)
    return cart


def test_add_items(cart):
    assert cart.get_total_items() == 7
    assert cart.get_item_count("apple") == 3


def test_remove_item(cart):
    cart.remove_item("apple", 2)
    assert cart.get_total_items() == 5
    assert cart.get_item_count("apple") == 1


def test_get_cart_items(cart):
    items = cart.get_cart_items()
    assert "apple" in items
    assert "banana" in items


def test_clear_cart(cart):
    items = cart.clear_cart()
    assert cart.get_total_items() == 0
    assert cart.get_cart_items() == []
