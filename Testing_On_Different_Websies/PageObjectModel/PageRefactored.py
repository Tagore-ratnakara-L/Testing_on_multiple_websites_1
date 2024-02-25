from Locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_string):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_type, locator_string))
            )
            return element
        except NoSuchElementException as e:
            print(f"Element with {locator_type} of {locator_string} not found", e)

    def get_text(self, locator_type, locator_string):
        element = self.get_element(locator_type, locator_string)
        return element.text

    def enter_text(self, locator_type, locator_string, text):
        self.get_element(locator_type, locator_string).send_keys(text)

    def click_button(self, locator_type, locator_string):
        self.get_element(locator_type, locator_string).click()

    def get_page_title(self):
        return self.driver.title


class MainPage(BasePage):

    def search(self, search_string):
        self.enter_text(*MainPageLocators.SEARCH_INPUT, search_string)
        self.click_button(*MainPageLocators.SEARCH_BUTTON)
