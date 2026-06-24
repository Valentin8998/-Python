from selenium.webdriver.common.by import By
import allure


class MainPage:
    """
    Этот класс отвечает за главную страницу сайта
    """

    def __init__(self, driver):
        self._driver = driver

    def MP(self):
        """
        Эта функция на добовление товаров в корзину
        """
        # Добавьте в корзину товары:
        # Sauce Labs Backpack.
        with allure.step("Добавить товар Sauce Labs Backpack в корзину"):
            self._driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-backpack'
                ).click()
        # Sauce Labs Bolt T-Shirt.
        with allure.step("Добавить товар Sauce Labs Bolt T-Shirt в корзину"):
            self._driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
                ).click()
        # Sauce Labs Onesie.
        with allure.step("Добавить товар Sauce Labs Onesie в корзину"):
            self._driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-onesie'
                ).click()

    def cart(self):
        """
        Эта функция для перехода в корзину
        """
        # Перейдите в корзину.
        with allure.step("Нажать на значок корзины"):
            self._driver.find_element(
                By.CLASS_NAME, 'shopping_cart_link').click()
