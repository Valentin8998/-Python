from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = (
     webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
)
driver.implicitly_wait(4)
driver.get('http://uitestingplayground.com/textinput')

pole = 'newButtonName'  # id
blue_button = 'updatingButton'  # id

driver.find_element(By.ID, pole).send_keys('SkyPro')

bb = driver.find_element(By.ID, blue_button)

bb.click()

txt = bb.text

print(txt)

driver.quit()
