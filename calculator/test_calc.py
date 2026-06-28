from calculator.input_delay import Delay
from calculator.button import Buttons
from calculator.result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure


@allure.title("Вычисление и сравнение")
@allure.description(
        "Вычисление заданного примера"
        " и сравнение его результата с заданым значением"
        )
@allure.feature("calculate")
@allure.severity("Critical")
def test_calculator():
    driver = (
     webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    )

    delay = Delay(driver)
    delay.input_delay()

    button = Buttons(driver)
    button.buttons()

    result = Result(driver)
    result.res()
    driver.quit()
