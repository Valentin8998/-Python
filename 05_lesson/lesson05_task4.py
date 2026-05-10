from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/login')

username = 'tomsmith'
password = 'SuperSecretPassword!'
username_loc = 'username'
password_loc = 'password'
login = 'fa'
grenn_button = 'flash'

driver.find_element(By.ID, username_loc).send_keys(username)

driver.find_element(By.ID, password_loc).send_keys(password)

driver.find_element(By.CLASS_NAME, login).click()

pri_nt = driver.find_element(By.ID, grenn_button)
# распечатка в консоле выбранного элемента в фортате текста
print(pri_nt.text)

driver.quit()
