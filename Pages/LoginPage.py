from Pages.BasePage import BasePage
from Configs import config


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config.amazon_urls["signin"])
