from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com')
driver.implicitly_wait(10)
img_element = driver.find_element(By.TAG_NAME,'img')

