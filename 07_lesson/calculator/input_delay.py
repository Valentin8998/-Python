from selenium.webdriver.common.by import By


class Delay:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver'
            '-java/slow-calculator.html'
        )

    def input_delay(self):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
