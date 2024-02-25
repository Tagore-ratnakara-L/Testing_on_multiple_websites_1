from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://python.org')
driver.maximize_window()
input_element = driver.find_element(By.NAME,"q")
print(input_element.tag_name)
print(input_element.get_attribute('placeholder'))
time.sleep(2)
input_element.send_keys('python news')
time.sleep(2)
Button = driver.find_element(By.ID, "submit")
print(Button.text)
Button.click()
time.sleep(2)
driver.back()
time.sleep(2)
input_element.clear()
driver.minimize_window()
time.sleep(5)
driver.close()


