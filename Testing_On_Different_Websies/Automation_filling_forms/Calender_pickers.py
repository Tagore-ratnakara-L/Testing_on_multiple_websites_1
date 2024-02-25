from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(2)
iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe_element)
time.sleep(2)
input_element = driver.find_element(By.ID, "datepicker")
input_element.click()
time.sleep(2)
Now = datetime.now()
Year = Now.year
Month = Now.month
Day = Now.day
# Date_path = f"//td[@data-month='{Month-1}'and @data-year= '{Year}']/a[@data-day = '{Day}']"
# Date_element = driver.find_element(By.XPATH, Date_path)
# print(Date_element.text)
# Date_element.click()
input_element.send_keys(f"{Month}/{Day}/{Year}")
# input_element.send_keys(f"{12}/{15}/{2024}")
input_element.click()
time.sleep(2)
driver.close()

