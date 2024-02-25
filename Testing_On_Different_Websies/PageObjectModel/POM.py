from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_page')
search_element = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Wikipedia']")
search_element.send_keys('Python')
time.sleep(2)
search_button = driver.find_element(By.XPATH,"//button[@class='cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button']")
search_button.click()
time.sleep(2)
python_link = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(4) > main:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(9) > li:nth-child(1) > a:nth-child(1)")
#python_link = None #Link for python not found !
assert python_link, "Link for python not found !"
python_link.click()

time.sleep(5)
driver.close()
