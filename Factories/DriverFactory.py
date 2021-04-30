from Resources.Browser import Browser
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(browser=Browser.chrome):
        """
        returns web driver instance

        :return: web driver
        """

        options = Options()
        options.add_argument('--start-maximized')

        if browser == Browser.chrome:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif browser == Browser.firefox:
            driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
        else:
            driver = webdriver.Ie(IEDriverManager().install(), options=options)

        return driver
