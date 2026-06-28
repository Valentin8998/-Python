from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class Delay:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver'
            '-java/slow-calculator.html'
        )

    def input_delay(self):
        """
        Эта функция делает два действия:
        1.Очищает поле со значением задержки вывода результата
        2.Вводит нужное значение задержки
        """
        with allure.step(
            "Очистить поле ввода для задержки вывода результата "
             ):
            self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        with allure.step("Ввести в поле значение 45"):
            self._driver.find_element(
                By.CSS_SELECTOR, '#delay').send_keys('5')
