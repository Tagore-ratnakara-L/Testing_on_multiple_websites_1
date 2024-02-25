from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/slider/')
iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe_element)
Slider_element = driver.find_element(By.ID, 'slider')
time.sleep(2)
Slider_element.click()
action = ActionChains(driver=driver)
time.sleep(2)
action.move_to_element_with_offset(Slider_element, 40, 0).click().perform()
time.sleep(2)
action.move_to_element_with_offset(Slider_element, -100, 0).click().perform()
time.sleep(2)
action.drag_and_drop_by_offset(Slider_element, 150, 0).perform()
time.sleep(5)
driver.close()
