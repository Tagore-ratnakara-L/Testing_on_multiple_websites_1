from selenium import webdriver
import time
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("https://selenium.dev")
element = d.find_elements(By.ID,"selenium_logo")
print(element)
time.sleep(5)
d.close()

