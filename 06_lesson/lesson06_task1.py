from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = (
     webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
)
# неЯвное ожидание
driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/ajax')

blue_button = '#ajaxButton'
grenn_button = 'bg-success'

driver.find_element(By.CSS_SELECTOR, blue_button).click()

gb = driver.find_element(By.CLASS_NAME, grenn_button).text
print(gb)

driver.quit()
