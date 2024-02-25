from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
book_element = driver.find_element(By.CSS_SELECTOR, "img[alt='Soumission']")
print(book_element.text)
print(book_element.tag_name)
book_element1 = driver.find_element(By.CSS_SELECTOR, "ol[class='row'] li:nth-child(1)")
print(book_element1.text)
print(book_element1.tag_name)
print(book_element1.size)
print(book_element1.screenshot('test.png'))
# img
# A Light in the ...
# £51.77
# In stock
# Add to basket
# li
# {'height': 410, 'width': 176}
# True
button_element = book_element1.find_element(By.CSS_SELECTOR,"button")
print(button_element.text)
print(button_element.get_attribute('type'))
# Add to basket
# submit
print(button_element.get_property('name'))
print(button_element.value_of_css_property('color'))
print(button_element.value_of_css_property('padding'))
# rgba(255, 255, 255, 1)
# 6px 12px
time.sleep(5)
driver.close()
driver.quit()
