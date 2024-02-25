from selenium import webdriver
from Training_ground_page import TrainingGroundPage

# Test setup

browser = webdriver.Chrome()
test_value = 'it worked'

# test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
# trng_page.button1.click()
browser.quit()
