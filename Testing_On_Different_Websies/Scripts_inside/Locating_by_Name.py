from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://python.org")
element = driver.find_element(By.NAME,"q")
print(element.tag_name)
print(element.get_attribute('class'))
element.clear()
element1 = driver.find_element(By.NAME,"keywords")
print(element1.tag_name)
print(element1.get_attribute('title') )


# input
# search-field
# meta
# Python programming language object oriented web free open source software license documentation download community
print(element1.get_attribute('content').split()) # content has been converted into list
#['Python', 'programming', 'language', 'object', 'oriented', 'web', 'free', 'open', 'source', 'software', 'license', 'documentation', 'download', 'community']
time.sleep(5)
driver.quit()
