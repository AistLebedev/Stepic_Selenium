from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
counter = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button1 = browser.find_element(By.ID, "book")
button1.click()
x = browser.find_element(By.ID, "input_value").text
input3 = browser.find_element(By.ID, "answer").send_keys(calc(x))
button = browser.find_element(By.ID, "solve")
button.click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text.split(': ')[-1])
browser.quit()
