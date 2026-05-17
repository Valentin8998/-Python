from selenium import webdriver
from selenium.webdriver.common.by import By


def test_saucedemo_checkout_total():
    """Тест проверки итоговой суммы в корзине SauceDemo"""

    # переменная для веб-драйвера firefox
    driver = webdriver.Firefox()

    try:
        driver.get('https://www.saucedemo.com/')
        driver.implicitly_wait(20)
        # Авторизация
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        # Добавьте в корзину товары:
        # Sauce Labs Backpack.
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        # Sauce Labs Bolt T-Shirt.
        driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        # Sauce Labs Onesie.
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        # Перейдите в корзину.
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        # Нажмите Checkout.
        driver.find_element(By.ID, 'checkout').click()
        # Заполните форму своими данными:
        # имя
        driver.find_element(By.ID, 'first-name').send_keys('Valentin')
        # фамилия
        driver.find_element(By.ID, 'last-name').send_keys('Dudko')
        # почтовый индекс
        driver.find_element(By.ID, 'postal-code').send_keys('142613')
        # Нажмите кнопку Continue.
        driver.find_element(By.ID, 'continue').click()
        # Прочитайте со страницы итоговую стоимость (Total).
        total_element = driver.find_element(
            By.CLASS_NAME, 'summary_total_label'
            )
        result = total_element.text  # "Total: $58.29"
        driver.close()
        # Проверьте, что итоговая сумма равна $58.29
        assert result == 'Total: $58.29', f"Ожидалось Total: $58.29, получено {
            result}"
    finally:
        # Закройте браузер
        driver.quit()
      
