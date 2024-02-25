import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
element = driver.find_element(By.CSS_SELECTOR,"div.alert.alert-warning")
print(element)
element1 = driver.find_elements(By.CSS_SELECTOR,"img")
for element2 in element1:
    print(element2.get_attribute('alt'))
time.sleep(5)
driver.close()