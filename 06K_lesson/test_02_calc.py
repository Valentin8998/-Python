from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = (
     webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
)
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

wait = WebDriverWait(driver, 46)
# Ждём, когда текст изменится на число (не пустое и не содержащее +)
wait.until(lambda d: d.find_element(By.CLASS_NAME, 'screen').text.isdigit())

screen = driver.find_element(By.CLASS_NAME, 'screen')
result = screen.text  # получаем текст (должно быть "15")
print(f"Результат на экране: {result}")

# Проверяем результат
assert result == '15', f"Ожидалось 15, получено {result}"

driver.quit()
