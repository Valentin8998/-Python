from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = (
     webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
    )
pic = 'award'  # id
# в переменной находится экземпляр с параметрами:
# 1 параметр - наш драйвер, 2 параметр - 40 секунд на ожидание
waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.visibility_of_element_located((By.ID, pic))
 )
# get_dom_attribute - возвращает значение атрибута без подстановки URL
src = driver.find_element(By.ID, pic).get_dom_attribute("src")
print(src)

driver.quit()
