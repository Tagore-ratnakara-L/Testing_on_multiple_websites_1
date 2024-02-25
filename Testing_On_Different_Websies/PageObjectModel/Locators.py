from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder='Search Wikipedia']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".cdx-button.cdx-button--action-default.cdx-button--framed.cdx-button--size-medium.cdx-button--weight-normal.cdx-search-input__end-button")
