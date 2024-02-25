from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://thegoldbugs.com')
driver.maximize_window()
time.sleep(2)
fieldset = driver.find_element(By.ID, "checkbox-b5b9cc19-24e5-4c8c-960a-055837723942")
print(fieldset.tag_name)
check_boxes = fieldset.find_elements(By.XPATH, '//input[@type ="checkbox"]')
checkbox1 = check_boxes[1]
print(checkbox1.get_attribute('value'))
print(checkbox1.is_selected())
checkbox1.click()
print(checkbox1.is_selected())
time.sleep(2)
checkbox1.click()
print(checkbox1.is_selected())
time.sleep(2)
# radio_buttons = driver.find_elements(By.XPATH, '//input[@type="radio"]')
# print(len(radio_buttons))
# radio_button1 = radio_buttons[0]
# # print(radio_button1.get_attribute('value'))
# # print(radio_button1.is_selected())
# radio_button1.click()
# # print(radio_button1.is_selected())
# # time.sleep(2)
# # radio_button2 = radio_buttons[1]
# # radio_button2.click()
# # print(radio_button1.is_selected())
# time.sleep(2)
driver.close()
