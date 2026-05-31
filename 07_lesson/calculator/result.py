from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Result:
    def __init__(self, driver):
        self._driver = driver

    def res(self):
        wait = WebDriverWait(self._driver, 46)
        # Ждём, когда текст изменится на число (не пустое и не содержащее +)
        wait.until(lambda d: d.find_element(
            By.CLASS_NAME, 'screen').text.isdigit())
        screen = self._driver.find_element(By.CLASS_NAME, 'screen')
        result = screen.text  # получаем текст (должно быть "15")
        print(f"Результат на экране: {result}")
        # Проверяем результат
        assert result == '15', f"Ожидалось 15, получено {result}"
