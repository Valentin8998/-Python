from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class Order:
    """
    Этот класс отвечает за заполнение анкеты и проверки итоговой стоймости
    """

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def YourInformation(self):
        """
        Ввод информации покупателя
        """
        with allure.step("Ввести в поле имя Valentin"):
            self._driver.find_element(
                By.ID, 'first-name').send_keys('Valentin')
            # фамилия
        with allure.step("Ввести в поле фамилия Dudko"):
            self._driver.find_element(By.ID, 'last-name').send_keys('Dudko')
            # почтовый индекс
        with allure.step("Ввести в поле индекс 142613"):
            self._driver.find_element(By.ID, 'postal-code').send_keys('142613')
            # Нажмите кнопку Continue.
        with allure.step("Нажать кнопку Continue"):
            self._driver.find_element(By.ID, 'continue').click()

    def result(self):
        """
        Проверка результата итоговой стоймости и заданного значения
        """
        # Прочитайте со страницы итоговую стоимость (Total).
        with allure.step("Прочитайте со страницы итоговую стоимость (Total)"):
            total_element = self._driver.find_element(
                By.CLASS_NAME, 'summary_total_label'
                    )
            result = total_element.text  # "Total: $58.29"
            self._driver.close()
        # Проверьте, что итоговая сумма равна $58.29
        with allure.step("Проверьте, что итоговая сумма равна $58.29"):
            assert result == 'Total: $58.29', (
                f"Ожидалось Total: $58.29, получено {result}"
            )
