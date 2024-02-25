from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
import time

driver = webdriver.Chrome()
driver.get('https://selenium-python.readthedocs.io/search.html?q=')
time.sleep(3)
submit = driver.find_element(By.NAME,'q')
time.sleep(3)
submit.send_keys('explicit wait')
time.sleep(3)
submit.submit()

Link_path = "//*[@id='search-results']/ul/li[1]/a"
try:
    result_element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, Link_path))
    )
    print(result_element.text)
except ElementNotVisibleException:
    print("Element not visible")
finally:
    time.sleep(3)
    driver.quit()
# 5. Waits