from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
link_element= driver.find_elements(By.XPATH,"//a[@title]")
for i in range(len(link_element)):
    print(link_element[i].get_attribute('title'))
    if i <= 10:
        print(link_element[i].get_attribute('title'))
        if i == 10:
            break
time.sleep(10)
driver.close()
driver.quit()

# A Light in the Attic
# A Light in the Attic
# Tipping the Velvet
# Tipping the Velvet
# Soumission
# Soumission
# Sharp Objects
# Sharp Objects
# Sapiens: A Brief History of Humankind
# Sapiens: A Brief History of Humankind
# The Requiem Red
# The Requiem Red
# The Dirty Little Secrets of Getting Your Dream Job
# The Dirty Little Secrets of Getting Your Dream Job
# The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
# The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
# The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
# The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
# The Black Maria
# The Black Maria
# Starving Hearts (Triangular Trade Trilogy, #1)
# Starving Hearts (Triangular Trade Trilogy, #1)