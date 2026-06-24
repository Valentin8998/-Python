from selenium.webdriver.common.by import By
import allure


class Auth:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    def authorization(self):
        """
        Эта функция для авторизации
        """
        with allure.step("Ввести в username 'standard_user'"):
            self.driver.find_element(
                By.ID, 'user-name').send_keys('standard_user')
        with allure.step("Ввести в password 'secret_sauce'"):
            self.driver.find_element(
                By.ID, 'password').send_keys('secret_sauce')
        with allure.step("нажать на кнопку 'login'"):
            self.driver.find_element(By.ID, 'login-button').click()
