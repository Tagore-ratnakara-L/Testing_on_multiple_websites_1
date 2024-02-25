from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
book_elements = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
len(book_elements)
book_elements[0].find_element(By.TAG_NAME, "img").get_attribute('alt')
price_list = []
for book in book_elements:
    price_list.append({
        'title': book.find_element(By.TAG_NAME, "img").get_attribute("alt"),
        'price': book.find_element(By.CSS_SELECTOR, "p.price_color").text
    })
i = 0
for i in range(len(price_list)):
    print(price_list[i])

# {'title': 'A Light in the Attic', 'price': '£51.77'}
# {'title': 'Tipping the Velvet', 'price': '£53.74'}
# {'title': 'Soumission', 'price': '£50.10'}
# {'title': 'Sharp Objects', 'price': '£47.82'}
# {'title': 'Sapiens: A Brief History of Humankind', 'price': '£54.23'}
# {'title': 'The Requiem Red', 'price': '£22.65'}
# {'title': 'The Dirty Little Secrets of Getting Your Dream Job', 'price': '£33.34'}
# {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 'price': '£17.93'}
# {'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 'price': '£22.60'}
# {'title': 'The Black Maria', 'price': '£52.15'}
# {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)', 'price': '£13.99'}
# {'title': "Shakespeare's Sonnets", 'price': '£20.66'}
# {'title': 'Set Me Free', 'price': '£17.46'}
# {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'price': '£52.29'}
# {'title': 'Rip it Up and Start Again', 'price': '£35.02'}
# {'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'price': '£57.25'}
# {'title': 'Olio', 'price': '£23.88'}
# {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'price': '£37.59'}
# {'title': 'Libertarianism for Beginners', 'price': '£51.33'}
# {'title': "It's Only the Himalayas", 'price': '£45.17'}