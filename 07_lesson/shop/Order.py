from selenium.webdriver.common.by import By


class Order:

    def __init__(self, driver):
        self._driver = driver

    def YourInformation(self):
        self._driver.find_element(By.ID, 'first-name').send_keys('Valentin')
        # фамилия
        self._driver.find_element(By.ID, 'last-name').send_keys('Dudko')
        # почтовый индекс
        self._driver.find_element(By.ID, 'postal-code').send_keys('142613')
        # Нажмите кнопку Continue.
        self._driver.find_element(By.ID, 'continue').click()

    def result(self):
        # Прочитайте со страницы итоговую стоимость (Total).
        total_element = self._driver.find_element(
            By.CLASS_NAME, 'summary_total_label'
                )
        result = total_element.text  # "Total: $58.29"
        self._driver.close()
        # Проверьте, что итоговая сумма равна $58.29
        assert result == 'Total: $58.29', f"Ожидалось Total: $58.29, получено {
            result}"
