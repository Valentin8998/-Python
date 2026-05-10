from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# переменная для веб-драйвера фаерфокс
driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/inputs')

stro = "input"

loc = driver.find_element(By.TAG_NAME, stro)

loc.send_keys(12345)

sleep(3)

loc.clear()

sleep(3)

loc.send_keys(54321)

sleep(3)

driver.quit()
