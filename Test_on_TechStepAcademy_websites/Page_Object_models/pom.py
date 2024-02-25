import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TrainingGroundPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        input = self.driver.find_element(By.ID, "ipt1")
        input.clear()
        input.send_keys(text)
        return None

    def get_input_text(self):
        input = self.driver.find_element(By.ID, "ipt1")
        elem_text = test_value
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element(By.ID, 'b1')
        button.click
        return None


# My test

# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
training_page = TrainingGroundPage(driver=browser)
training_page.go()
time.sleep(3)
training_page.type_into_input(test_value)
# training_page.click_button_1()
text_from_input = training_page.get_input_text()
assert text_from_input == test_value
