from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://thegoldbugs.com')
driver.maximize_window()
radio_button = driver.find_element(By.CSS_SELECTOR, '.item .LluRZBfpqUL7wzCTknH5:nth-child(6) .dUT6sxBZ0jpqdKQD7OIA')
# print(len(radio_buttons))
# radio_button1 = radio_buttons[0]
# radio_button2 = radio_buttons[1]
# print(radio_button1.get_attribute('value'))
# print(radio_button1.is_selected())
radio_button.click()
# print(radio_button1.is_selected())
# time.sleep(2)
# radio_button2 = radio_buttons[1]
# radio_button2.click()
# print(radio_button1.is_selected())
time.sleep(2)
driver.close()