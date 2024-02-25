from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/" + 'draggable')
#driver.find_element(By.ID,"draggable") # this throws error since we are out of frame yet
iframe_element = driver.find_element(By.CSS_SELECTOR,"iframe.demo-frame")
driver.switch_to.frame(iframe_element)
drag_element = driver.find_element(By.ID,"draggable")
print(drag_element.tag_name)#div
driver.switch_to.default_content()
main_nav= driver.find_element(By.ID,"main")
print(main_nav.tag_name)#nav
time.sleep(6)
driver.close()
