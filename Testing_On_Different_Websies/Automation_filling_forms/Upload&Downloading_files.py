import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://python.org/downloads/')
# Download_element = driver.find_element(By.XPATH,"//div[@class='download-os-windows']//a[@class='button'][normalize-space()='Download Python 3.12.0']")
# Download_element.click()
# DOWNLOAD_DIR = 'C:\\Users\\Ratnakar'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('prefs',
#                                 {'download.default_directory': DOWNLOAD_DIR
#                                 })
# driver = webdriver.Chrome(options=options)
# driver.get('https://python.org/downloads/')
# Download_element = driver.find_element(By.XPATH,"//div[@class='download-os-windows']//a[@class='button'][normalize-space()='Download Python 3.12.0']")
# Download_element.click()
# time.sleep(20)
# driver.quit()

driver = webdriver.Chrome()
driver.get('https://imgur.com/upload')
Upload_element = driver.find_element(By.ID,'file-input')
print(Upload_element.tag_name)
Upload_element.send_keys('C:\\Users\\Ratnakar\\FB_IMG_1515778558901.jpg')
time.sleep(20)
driver.quit()

