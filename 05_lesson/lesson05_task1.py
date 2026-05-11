# строка импорта
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# переменная для веб-драйвера хрома
driver = webdriver.Chrome()
# команда для открытия страницы
driver.get('http://uitestingplayground.com/classattr')
# переменная локатора
blue_button = 'btn-primary'
# запрос на возрат нужного локатора
loc = driver.find_element(By.CLASS_NAME, blue_button)
# клик по заданной переменной, можно указать в конце запроса на возрат локатора
loc.click()
# позволяет принять и закрыть всплывающее окно после клика
driver.switch_to.alert.accept()
# сколько секунд будет открыта страница до закрытия, можно использовать между
# действиями для отслеживания действий скрипта
sleep(2)
