from Locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_string):
        return self.driver.find_element(locator_type, locator_string)

    def get_text(self, locator_type, locator_string):
        element = self.get_element(locator_type, locator_string)
        return element.text

    def enter_text(self, locator_type, locator_string, text):
        self.get_element(locator_type, locator_string).send_keys(text)

    def click_button(self, locator_type, locator_string):
        self.get_element(locator_type, locator_string).click

    def get_page_title(self):
        return self.driver.title


class MainPage(BasePage):

    def search(self, search_string):
        self.enter_text(*MainPageLocators.SEARCH_INPUT, search_string)
        self.click_button(*MainPageLocators.SEARCH_BUTTON)
