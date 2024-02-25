from selenium import webdriver
# from selenium.webdriver.chrome import service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

# mobile_emulation = {'deviceName': 'iphone 12 Pro'}
# driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('mobileEmulation', {'deviceName': 'iphone 12 Pro'})
# driver = webdriver.Chrome(service=service,options=ChromeOptions)
driver = webdriver.Chrome(options=ChromeOptions)
driver.get('https://selenium.dev')
