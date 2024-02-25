from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/" + 'draggable')
driver.refresh()
time.sleep(2)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
time.sleep(2)
driver.back()
time.sleep(2)
driver.get('https://python.org')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
