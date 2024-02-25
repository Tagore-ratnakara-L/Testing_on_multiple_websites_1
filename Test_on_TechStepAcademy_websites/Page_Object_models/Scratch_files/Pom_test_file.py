from selenium import webdriver

from Training_ground_test import TrainingGroundPage


# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
trng_page.button1.click