from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    def MP(self):
        # Добавьте в корзину товары:
        # Sauce Labs Backpack.
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack'
            ).click()
        # Sauce Labs Bolt T-Shirt.
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        # Sauce Labs Onesie.
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie'
            ).click()

    def cart(self):
        # Перейдите в корзину.
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
