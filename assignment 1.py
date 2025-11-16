import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

login_data = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")]

@pytest.mark.parametrize("username,password", login_data)
def test_saucedemo_flow(username, password):
    options = Options()
    service = Service(r"C:\Users\subhandari\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)


        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        products[0].find_element(By.TAG_NAME, "button").click()
        products[1].find_element(By.TAG_NAME, "button").click()
        time.sleep(1)


        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")


        cart_items[0].find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")


        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)


        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        products[2].find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        time.sleep(1)


        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

    finally:
        driver.quit()