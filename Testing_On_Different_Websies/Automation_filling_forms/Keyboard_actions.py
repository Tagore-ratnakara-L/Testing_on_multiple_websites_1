import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://selenium.dev/documentation/webdriver/')
search_element = driver.find_element(By.CSS_SELECTOR,"span.DocSearch-Button-Placeholder")
# search_element.click()
time.sleep(2)
action = ActionChains(driver=driver)
action.key_down(Keys.CONTROL).send_keys('k').release().perform()
input_element = driver.find_element(By.ID,'docsearch-input')
input_element.send_keys('webDriver')
time.sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
action.send_keys(Keys.ARROW_UP).perform()
time.sleep(2)
action.send_keys(Keys.ESCAPE).perform()
time.sleep(2)
action.key_down(Keys.CONTROL).send_keys('k').key_up(Keys.CONTROL).release().perform()
time.sleep(5)
driver.close()




