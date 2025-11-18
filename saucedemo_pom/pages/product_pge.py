from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_by_index(self, index):
        products = self.driver.find_elements(*self.inventory_items)
        products[index].find_element(By.TAG_NAME, "button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()