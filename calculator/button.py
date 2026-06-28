from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class Buttons:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def buttons(self):
        """
        Эта функция отвечает за нажатие кнопок в калькуляторе
        """
        with allure.step("нажать на кнопку с значением 7"):
            self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        with allure.step("нажать на кнопку с значением +"):
            self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        with allure.step("нажать на кнопку с значением 8"):
            self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        with allure.step("нажать на кнопку с значением ="):
            self._driver.find_element(By.XPATH, "//span[text()='=']").click()
