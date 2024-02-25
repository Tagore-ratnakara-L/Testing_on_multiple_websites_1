from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
element = driver.find_element(By.LINK_TEXT,"Tipping the Velvet")
print(element)
print(element.text)
print(element.tag_name)
print(element.location)

time.sleep(5)
driver.close()
driver.quit()
# element="31133BEC5F4854C5C440B35DFD666A84_element_30")>
# Tipping the Velvet
# a
# {'x': 494, 'y': 643}
