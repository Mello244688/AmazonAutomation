from Pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url
        self.driver.get(url)
