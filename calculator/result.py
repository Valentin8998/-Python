from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure


class Result:
    def __init__(self, driver):
        self._driver = driver

    def res(self):
        """
        Эта функция делает слудующие:
        1.Ждёт, когда текст изменится на число (не пустое и не содержащее +)
        2.Получает результат и записывает в переменную "result"
        3.Сравнивает результат в переменной "result" с строкой '15'
        """
        wait = WebDriverWait(self._driver, 46)
        wait.until(lambda d: d.find_element(
            By.CLASS_NAME, 'screen').text.isdigit())
        screen = self._driver.find_element(By.CLASS_NAME, 'screen')
        with allure.step("получаем результат в виде текста ,должно быть 15"):
            result = screen.text
        print(f"Результат на экране: {result}")
        with allure.step("сравниваем результат с 15"):
            assert result == '15', f"Ожидалось 15, получено {result}"
