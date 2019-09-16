from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_INPUT_FOR_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT_FOR_LOGIN = (By.CSS_SELECTOR, "[name='login-password']")
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "p>a")
    LOGIN_BUTTON = (By.TAG_NAME, "[name='login_submit']")
    EMAIL_INPUT_FOR_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_FOR_REG = (By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWORD_INPUT_FOR_CONFIRM_REG = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_BUTTON = (By.TAG_NAME, "[name='registration_submit']")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT_BEFORE = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_BEFORE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT_AFTER = (By.XPATH, "//div[@class='alertinner ']/p[1]/strong")
    NAME_PRODUCT_AFTER = (By.XPATH, "//div[@class='alertinner ']/strong[1]")
