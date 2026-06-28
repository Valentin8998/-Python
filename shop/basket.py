from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class Basket:
    """
    Этот класс для корзины покупок
    """
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def checkout(self):
        with allure.step("Кликнуть на кнопку checkout"):
            self._driver.find_element(By.ID, 'checkout').click()
