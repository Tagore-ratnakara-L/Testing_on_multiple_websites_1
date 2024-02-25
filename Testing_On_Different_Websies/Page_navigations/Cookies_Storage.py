from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://python.org')
#print(driver.get_cookies())
driver.add_cookie({
    'name': 'my new_cookie',
    'value': 'Hey! look at my cookie'
} )
driver.execute_script("window.localStorage.setItem('key1','value1')")
print(driver.execute_script("return window.localStorage.getItem('key1')"))
driver.execute_script("window.sessionStorage.setItem('key2','value2')")
print(driver.execute_script("return window.sessionStorage.getItem('key2')"))
time.sleep(4)

# value1
# value2