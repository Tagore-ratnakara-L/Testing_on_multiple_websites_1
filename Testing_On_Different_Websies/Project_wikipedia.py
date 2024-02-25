from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
F_today_featured_article = 'div#mp-tfa'
Did_you_know = 'div#mp-dyk'
In_the_news = 'div#mp-itn'
On_this_day = 'div#mp-otd'
locator_list = [
    F_today_featured_article, Did_you_know, In_the_news, On_this_day
]
link_dictionary = {}
for locator in locator_list:
    div_element = driver.find_element(By.CSS_SELECTOR, locator)
    info_list = []
    for link in div_element.find_elements(By.TAG_NAME, 'a'):
        info_dict = {
            'title': link.get_attribute('title'),
            'text': link.text,
            'href': link.get_attribute('href')
        }
        info_list.append(info_dict)
        link_dictionary[locator] = info_list
print(f'{link_dictionary[F_today_featured_article]}\n')
for key,value in link_dictionary.items():
    print(f'{key}- {len(value)} links')
    # div  # mp-tfa- 21 links
    # div  # mp-dyk- 18 links
    # div  # mp-itn- 28 links
    # div  # mp-otd- 37 links
time.sleep(8)
driver.close()
driver.quit()
