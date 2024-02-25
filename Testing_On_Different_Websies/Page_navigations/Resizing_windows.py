from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.get("https://python.org")
# print(driver.get_window_size())  # {'width': 1051, 'height': 798}
# print(driver.get_window_position())  # {'x': 9, 'y': 9}
# print(driver.get_window_rect())  # {'height': 798, 'width': 1051, 'x': 9, 'y': 9}
# time.sleep(3)
# driver.maximize_window()
# print(driver.get_window_size())  # {'width': 1552, 'height': 832}
# print(driver.get_window_position())  # {'x': -8, 'y': -8}
# print(driver.get_window_rect())  # {'height': 832, 'width': 1552, 'x': -8, 'y': -8}
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.set_window_size(width= 1600, height= 800)
time.sleep(3)
driver.set_window_position(x= -7, y= -9)
time.sleep(3)
driver.set_window_rect(x=8, y=8, height=950, width=1100)
time.sleep(3)
driver.close()
