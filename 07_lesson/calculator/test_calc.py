from input_delay import Delay
from buttons import Buttons
from result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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
