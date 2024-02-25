from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://thegoldbugs.com')
driver.maximize_window()
select_element = driver.find_element(By.ID,"select-e1f50715-c8a7-48eb-bc99-2c245676068c-field")
# print(select_element.text)
# select_element.click()
option_elements = select_element.find_elements(By.TAG_NAME,"option")
for element in option_elements:
    print(f'{element.text}:{element.get_attribute("value")}')
# Select an option:
# Google:Google
# Facebook:Facebook
# Instagram:Instagram
# Other:Other
option_elements[-1].click()
time.sleep(2)
select_element.click()
time.sleep(2)
option_elements[1].click()
time.sleep(2)
select = Select(select_element)
print([option.text for option in select.options]) #['Google', 'Facebook', 'Instagram', 'Other']
select.select_by_index(3)
time.sleep(2)
select.select_by_visible_text('Facebook')
time.sleep(2)
driver.close()


