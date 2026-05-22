from authorization import Auth
from selenium import webdriver
from MainPage import MainPage
from basket import Basket
from Order import Order

driver = webdriver.Firefox()
auth = Auth(driver)
auth.authorization()

mainpage = MainPage(driver)
mainpage.MP()
mainpage.cart()

basket = Basket(driver)
basket.checkout()

order = Order(driver)
order.YourInformation()
order.result()

driver.quit()
