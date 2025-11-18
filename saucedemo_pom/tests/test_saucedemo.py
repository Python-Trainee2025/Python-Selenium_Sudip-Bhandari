import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import time

login_data = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
]

@pytest.mark.parametrize("username,password", login_data)
def test_saucedemo_flow(driver, username, password):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(username, password)
    time.sleep(2)

    products_page.add_product_by_index(0)
    products_page.add_product_by_index(1)
    time.sleep(1)

    products_page.go_to_cart()
    time.sleep(1)

    cart_page.remove_item_by_index(0)
    time.sleep(1)

    cart_page.continue_shopping()
    time.sleep(1)

    products_page.add_product_by_index(2)
    products_page.go_to_cart()
    time.sleep(1)
