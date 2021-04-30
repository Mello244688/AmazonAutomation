import sys

import keyring
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Factories.DriverFactory import DriverFactory
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Configs import config as cfg
from Resources.Locators import Locators


def main():
    driver = DriverFactory.get_driver(cfg.browsers["default_browser"])
    locators = Locators()

    login(locators, LoginPage(driver))

    # check for product arg and make sure the key is in the dict
    if len(sys.argv) >= 1 and cfg.amazon_urls.get(sys.argv[1]) is not None:
        product = cfg.amazon_urls.get(sys.argv[1])
    else:
        product = cfg.amazon_urls["soy_sauce"]

    product_page = ProductPage(driver, product)

    # if purchase unsuccessful, keep trying
    while not buy_product(locators, product_page):
        product_page.driver.refresh()

    driver.close()
    sys.exit(0)


def buy_product(locators, product_page):
    # check for buy now button
    if product_page.does_element_exist(locators.PRODUCT_BUY_NOW_BUTTON, 1):

        # check for pop out ad close button
        if product_page.does_element_exist(locators.AOD_CLOSE, .01):
            ActionChains(product_page.driver).send_keys(Keys.ESCAPE).perform()

        # click buy now button
        product_page.click(locators.PRODUCT_BUY_NOW_BUTTON)

        # check for frame and switch to it if available
        if product_page.does_element_exist(locators.PRODUCT_TURBO_CHECKOUT_FRAME):
            print("switched to frame")
            product_page.switch_to_frame(locators.PRODUCT_TURBO_CHECKOUT_FRAME)

            # check that the place order button exists and click it
            if product_page.does_element_exist(locators.PRODUCT_TURBO_CHECKOUT_BUTTON):
                product_page.click(locators.PRODUCT_TURBO_CHECKOUT_BUTTON)

        # frame did not popup, redirected to checkout. Check for place order button and click it
        elif product_page.does_element_exist(locators.CHECKOUT_PLACE_ORDER_BUTTON):
            product_page.click(locators.CHECKOUT_PLACE_ORDER_BUTTON)

    # return false if buy now does not exist
    else:
        return False

    return product_page.does_element_exist(locators.CHECKOUT_CONFIRMATION_STATUS)


def login(locators, login_page):
    # check for username textbox and enter username if it exists
    if login_page.does_element_exist(locators.LOGIN_USERNAME_TEXT_BOX):
        login_page.enter_text(locators.LOGIN_USERNAME_TEXT_BOX, cfg.amazon_keyring["username"])

        # check for continue button to enter password and click it
        if login_page.does_element_exist(locators.LOGIN_CONTINUE_BUTTON):
            login_page.click(locators.LOGIN_CONTINUE_BUTTON)

    # check for password checkbox and enter password
    if login_page.does_element_exist(locators.LOGIN_PASSWORD_TEXT_BOX):
        login_page.enter_text(
            locators.LOGIN_PASSWORD_TEXT_BOX,
            keyring.get_password(cfg.amazon_keyring["service_name"], cfg.amazon_keyring["username"]))

    # check for signin button and click it
    if login_page.does_element_exist(locators.LOGIN_SIGNIN_BUTTON):
        login_page.click(locators.LOGIN_SIGNIN_BUTTON)

    # waiting until page loads
    if login_page.is_visible(locators.NAV_LINK):
        print("logged in")


if __name__ == '__main__':
    main()
