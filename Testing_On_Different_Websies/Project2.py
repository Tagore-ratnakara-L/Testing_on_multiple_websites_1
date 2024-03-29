from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://thegoldbugs.com')
driver.maximize_window()
form_element = driver.find_element(By.TAG_NAME, 'form')
fname_name = driver.find_element(By.NAME, 'fname')
time.sleep(2)
fname_name.send_keys('L')
time.sleep(2)
lname_element = driver.find_element(By.NAME, 'lname')
lname_element.send_keys('Ratna')
time.sleep(2)
email_element = driver.find_element(By.ID, 'email-yui_3_17_2_1_1664570076619_2728-field')
email_element.send_keys('ltrao2015@gmail.com')
time.sleep(2)
Subject_element = driver.find_element(By.ID, 'text-yui_3_17_2_1_1664570076619_2729-field')
Subject_element.send_keys('Have fun yayyy!')
time.sleep(2)
message_element = driver.find_element(By.TAG_NAME, 'textarea')
message_element.send_keys('You are Handsome Bro!')
time.sleep(2)
checkbox_element = driver.find_element(By.NAME, 'checkbox-b5b9cc19-24e5-4c8c-960a-055837723942-field')
checkbox_element.click()
print(checkbox_element.is_selected())
time.sleep(2)
Radio_element = driver.find_element(By.CSS_SELECTOR,
                                    'body > div:nth-child(1) > div:nth-child(5) > main:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(2) > fieldset:nth-child(6) > div:nth-child(3) > label:nth-child(1) > span:nth-child(2)')
Radio_element.click()
time.sleep(2)
select_element = driver.find_element(By.ID, 'select-e1f50715-c8a7-48eb-bc99-2c245676068c-field')
select_element.click()
select = Select(select_element)
print(option.text for option in select.options)
time.sleep(2)
select.select_by_value('Google')
time.sleep(2)
select.select_by_visible_text('Other')
time.sleep(2)
survey_radio = driver.find_element(By.XPATH, "//label[normalize-space()='Strongly Agree']")
survey_radio.click()
time.sleep(2)
form_element.submit()
time.sleep(5)
driver.close()
