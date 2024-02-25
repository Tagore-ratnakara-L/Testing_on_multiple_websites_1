from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')
iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')
driver.switch_to.frame(iframe_element)
action = ActionChains(driver=driver)
Src_element = driver.find_element(By.ID, 'draggable')
Target_element = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(Src_element, Target_element).perform()
action.drag_and_drop_by_offset(source=Src_element,xoffset=20,yoffset=0).perform()
time.sleep(5)
driver.close()
