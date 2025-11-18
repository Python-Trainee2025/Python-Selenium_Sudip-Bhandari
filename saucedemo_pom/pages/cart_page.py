from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_btn = (By.ID, "continue-shopping")

    def remove_item_by_index(self, index):
        items = self.driver.find_elements(*self.cart_items)
        items[index].find_element(By.TAG_NAME, "button").click()

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_btn).click()