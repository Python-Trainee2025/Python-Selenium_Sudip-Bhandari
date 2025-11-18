import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

@pytest.fixture
def driver():
    options = Options()
    service = Service(r"C:\Users\subhandari\Downloads\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()