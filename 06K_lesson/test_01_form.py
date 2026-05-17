from selenium import webdriver
from selenium.webdriver.common.by import By
# альтернатива запуска Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


edge_options = Options()
driver = webdriver.Edge(options=edge_options)
driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
        )

First_name = '[name="first-name"]'
Last_name = '[name="last-name"]'
Address = '[name="address"]'
Email = '[name="e-mail"]'
Phone_number = '[name="phone"]'
Zip = '[name="zip-code"]'
City = '[name="city"]'
Country = '[name="country"]'
job_position = '[name="job-position"]'
Company = '[name="company"]'
Submit = '[type="submit"]'

driver.find_element(By.CSS_SELECTOR, First_name).send_keys('Иван')
driver.find_element(By.CSS_SELECTOR, Last_name).send_keys('Петров')
driver.find_element(By.CSS_SELECTOR, Address).send_keys('Ленина, 55-3')
driver.find_element(By.CSS_SELECTOR, Email).send_keys('test@skypro.com')
driver.find_element(
        By.CSS_SELECTOR, Phone_number).send_keys('+7985899998787'
                                                 )
driver.find_element(By.CSS_SELECTOR, City).send_keys('Москва')
driver.find_element(By.CSS_SELECTOR, Country).send_keys('Россия')
driver.find_element(By.CSS_SELECTOR, job_position).send_keys('QA')
driver.find_element(By.CSS_SELECTOR, Company).send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, Submit).click()

wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд
wait.until(EC.visibility_of_element_located((By.ID, 'zip-code')))

zip_code_field = driver.find_element(By.ID, 'zip-code')
background_color = zip_code_field.value_of_css_property('background-color')
# проверка фактического цвета для assert
# print(f"Реальный цвет поля Zip: {background_color}")
assert '248, 215, 218' in background_color  # проверка на красный цвет

grenns = [
    'first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country',
    'job-position', 'company'
]

wait = WebDriverWait(driver, 10)

# Проверяем каждое поле отдельно
for field_id in grenns:
    field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    background_color = field.value_of_css_property('background-color')
    # print(f"Цвет поля {field_id}: {background_color}")
    assert '209, 231, 221' in background_color

driver.quit()
