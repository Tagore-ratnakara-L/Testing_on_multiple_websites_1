from selenium.webdriver.support.select import Select
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class BasePage(object):
    """Base class to initialize the base page to call all the pages """

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_string):
        """Get element from page"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_type, locator_string))
            )
            return element
        except NoSuchElementException as e:
            print(f"Element with {locator_type} of {locator_string} Not found ", e)

    def get_text(self, locator_type, locator_string):
        """Get text of page element"""
        element = self.get_element(locator_type, locator_string)
        return element.text

    def enter_text(self, locator_type, locator_string, text):
        """Enter text into page element """
        self.get_element(locator_type, locator_string).send_keys(text)

    def click(self, locator_type, locator_string):
        """Click button on page"""
        try:
            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((locator_type,locator_string))
            ).click()

        except ElementClickInterceptedException as e:
            print(f"Element click intercepted for {locator_type} of {locator_string}", e)

    def select_by_value(self, locator_type, locator_string, value):
        """Select option in dropdown menu based on value"""
        select = Select(self.get_element(locator_type, locator_string))
        select.select_by_value(value)

    def submit_form(self, locator_type, locator_string):
        """Submit form element"""
        self.get_element(locator_type, locator_string).submit()


class MainPage(BasePage):
    """Class for actions on the web page """

    def click_booking_form_link(self):
        """Click on the booking form link """
        self.click(*MainPageLocators.BOOKING_FORM_ANCHOR)

    def fill_required_fields(self):
        """fill out only required fields in the form """
        self.enter_text(*MainPageLocators.FIRST_NAME, "Ratnakara")
        self.enter_text(*MainPageLocators.LAST_NAME, "Rao")
        self.enter_text(*MainPageLocators.EMAIL, "ltrao2015@gmail.com")
        self.enter_text(*MainPageLocators.SUBJECT, "Love your band!")

    def fill_non_required_fields(self):
        """fill out only Non - required fields in the form """
        self.enter_text(*MainPageLocators.MESSAGE, "Good Band at All!")
        self.click(*MainPageLocators.NO_RESPONSE_CHECKBOX)
        self.click(*MainPageLocators.PUBLIC_SHOW_RADIO_BTN)
        self.select_by_value(*MainPageLocators.SELECT_DROPDOWN, "Other")
        self.click(*MainPageLocators.SURVEY_RADIO_BTN)

    def fill_all_fields(self):
        """Fill both required and Non - required fields in the form"""
        self.fill_required_fields()
        self.fill_non_required_fields()

    def submit_gold_bugs_form(self):
        """Submit booking form"""
        self.submit_form(*MainPageLocators.FORM_ELEMENT)

    def get_form_failure_div(self):
        """Get the div with the error message on failed form from submission """
        return self.get_element(*MainPageLocators.FORM_FAILURE_DIV)

    def get_form_success_div(self):
        """Get the div with the 'Thank you!'Success message on form from submission """
        return self.get_element(*MainPageLocators.FORM_SUCCESS_DIV)
