from selenium.webdriver.common.by import By


class Locators:
    # login page locators
    LOGIN_USERNAME_TEXT_BOX = (By.ID, "ap_email")
    LOGIN_CONTINUE_BUTTON = (By.ID, "continue")
    LOGIN_PASSWORD_TEXT_BOX = (By.ID, "ap_password")
    LOGIN_SIGNIN_BUTTON = (By.ID, "signInSubmit")

    # product page locators
    PRODUCT_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    PRODUCT_BUY_NOW_BUTTON = (By.ID, "buy-now-button")
    PRODUCT_TITLE = (By.ID, "productTitle")
    PRODUCT_TURBO_CHECKOUT_BUTTON = (By.ID, "turbo-checkout-pyo-button")
    PRODUCT_TURBO_CHECKOUT_FRAME = (By.ID, "turbo-checkout-iframe")

    # nav locators
    NAV_LINK = (By.ID, "nav-logo-sprites")

    # checkout locators
    CHECKOUT_PLACE_ORDER_BUTTON = (By.NAME, "placeYourOrder1")
    CHECKOUT_CONFIRMATION_STATUS = (By.ID, "widget-purchaseConfirmationStatus")

    # ad locators
    AOD_CLOSE = (By.ID, "aod-close")
