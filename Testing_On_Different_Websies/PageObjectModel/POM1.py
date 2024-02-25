from selenium import webdriver

import unittest

from PageRefactored import MainPage


class WikipediaMainPageSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://en.wikipedia.org/wiki/Main_Page')

    def test_search(self):
        search_text = 'Python (programming language)'
        main_page = MainPage(self.driver)
        main_page.search(search_text)
        self.assertEqual(search_text + ' - Wikipedia', main_page.get_page_title())
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
