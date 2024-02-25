from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
driver.execute_script("alert('Hey! this is an alert')")  # faking an alert
time.sleep(4)
alert = driver.switch_to.alert
print(alert.text)  # Hey! this is an alert
alert.accept()
driver.execute_script("confirm('Hey!Do you want to confirm? ')")
time.sleep(4)
alert1 = driver.switch_to.alert
print(alert1.text)  # Hey!Do you want to confirm?
alert1.dismiss()
time.sleep(4)
driver.close()
