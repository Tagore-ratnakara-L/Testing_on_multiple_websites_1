import unittest

from selenium import webdriver
from page import MainPage


class GoldBugsMainPageFormFill(unittest.TestCase):
    """Class for testing form filling functionality from Gold bugs home page"""

    def setUp(self) -> None:
        """Test-level set-up method"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.thegoldbugs.com")

    def test_invalid_form_submission(self):
        """Place holder test methods """
        main_page = MainPage(self.driver)
        main_page.click_booking_form_link()
        main_page.fill_non_required_fields()
        main_page.submit_gold_bugs_form()
        self.assertIsNotNone(main_page.get_form_failure_div(), 'Alert for required fields are missing')

    def test_valid_form_submissions(self):
        """Valid form submission Case"""
        main_page = MainPage(self.driver)
        main_page.click_booking_form_link()
        main_page.fill_all_fields()
        main_page.submit_gold_bugs_form()
        self.assertIsNotNone(main_page.get_form_success_div(), 'Form was not submitted successful')

    def tearDown(self):
        """Test-level tear down method """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

