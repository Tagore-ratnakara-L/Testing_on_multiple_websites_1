from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/')
buttons = driver.find_elements(By.TAG_NAME,"button")
print(len(buttons))
button1 = buttons[0]
print(button1.text)
# button1.click()
actions = ActionChains(driver)
actions.context_click(on_element=button1).perform()
time.sleep(3)
actions.click_and_hold(on_element=button1).perform()
actions.release().perform()
time.sleep(3)
link_element = driver.find_element(By.TAG_NAME,'a')
print(link_element.text)
link_element.click()
time.sleep(3)
driver.close()
