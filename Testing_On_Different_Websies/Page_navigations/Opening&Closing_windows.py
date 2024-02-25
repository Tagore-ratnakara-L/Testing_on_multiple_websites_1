from selenium import webdriver
import time

#Accessing two windows one after other
# driver = webdriver.Chrome()
# driver.get('https://python.org')
# time.sleep(4)
# driver.switch_to.new_window('window')
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# time.sleep(4)
# driver.close()

driver = webdriver.Chrome()
driver.get('https://python.org')
# time.sleep(10)
driver1 = webdriver.Chrome()
driver1.get('https://en.wikipedia.org/wiki/Main_Page')
# time.sleep(5)
quit()
# driver.close()
# time.sleep(2)
# driver1.close()
