from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """class with locators in web page """

    # required field
    FIRST_NAME = (By.NAME, "fname")
    LAST_NAME = (By.NAME, "lname")
    EMAIL = (By.ID, "email-yui_3_17_2_1_1664570076619_2728-field")
    SUBJECT = (By.ID, "text-yui_3_17_2_1_1664570076619_2729-field")

    # Non - required fields
    MESSAGE = (By.TAG_NAME, "textarea")
    NO_RESPONSE_CHECKBOX = (By.XPATH, "//input[@value='No Response Required']")
    PUBLIC_SHOW_RADIO_BTN = (By.CSS_SELECTOR, '.option:nth-child(3) .hRT9UlCFgnP8dgzh7Azj')
    SELECT_DROPDOWN = (By.ID, "select-e1f50715-c8a7-48eb-bc99-2c245676068c-field")
    SURVEY_RADIO_BTN = (By.CSS_SELECTOR, '.item .LluRZBfpqUL7wzCTknH5:nth-child(6) .dUT6sxBZ0jpqdKQD7OIA')

    # other elements
    FORM_ELEMENT = (By.XPATH, "//button[@type='submit']")
    FORM_FAILURE_DIV = (By.CSS_SELECTOR, ".field-list > .title > .form-field-error.mkTKK6Se1WSWC0Psa20C > svg[role='presentation']")
    FORM_SUCCESS_DIV = (By.CSS_SELECTOR, "div.form-submission-text")
    BOOKING_FORM_ANCHOR = (By.XPATH, "//div[@id='headerNav']//a[normalize-space()='Booking Form']")
    # FORM_ELEMENT = (By.TAG_NAME, 'form')
    # FORM_FAILURE_DIV = (By.CSS_SELECTOR, 'div.field-error')
    # FORM_SUCCESS_DIV = (By.CSS_SELECTOR, 'div.form-submission-text')
    # BOOKING_FORM_ANCHOR = (By.XPATH, '/html/body/div[1]/header/div/div[2]/div/nav/div[4]/a')

