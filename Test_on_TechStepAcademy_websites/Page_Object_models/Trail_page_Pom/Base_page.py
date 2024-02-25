class BasePage(object):

    def __init__(self,driver):
        self.driver = driver


    def go(self):
        self.driver.get(self.url)