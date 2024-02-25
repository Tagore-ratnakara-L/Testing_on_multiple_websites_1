from selenium import webdriver

from trial_page import TrialPage

# Page setup
browser = webdriver.Chrome()

# TrailPage Test
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text('rock')
trial_page.stone_button.click()

input()
browser.quit()