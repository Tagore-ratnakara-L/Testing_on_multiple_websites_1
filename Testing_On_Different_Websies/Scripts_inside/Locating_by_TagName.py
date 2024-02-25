from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
link_element = driver.find_elements(By.TAG_NAME,"a")
for link in link_element:
    i = (link.text)
    print(link.text or link.get_attribute('title'))
    print(link.get_attribute('href'))

    if i == 'Soumission':
        break

time.sleep(5)
driver.close()
