import send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
import time

# opts = webdriver.ChromeOptions()
# opts.add_argument('--disable-gpu')
Options = webdriver.ChromeOptions()
Options.add_experimental_option("detach",True)
#browser1 = webdriver.Chrome(options=Options)
browser2 = webdriver.Chrome(options=Options)

#browser1.get('https://techstepacademy.com/training-ground')
browser2.get('https://google.com')
search = browser2.find_element(By.ID,"APjFqb")
search.click()
search.send_keys("Youtube")

time.sleep(5)
