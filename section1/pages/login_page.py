from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_FOR_LOGIN) and \
               self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_FOR_LOGIN) and\
               self.is_element_present(*LoginPageLocators.LINK_FORGOT_PASSWORD) and \
               self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Items not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT_FOR_REG) and\
               self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_FOR_REG) and\
               self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_FOR_CONFIRM_REG) and\
               self.is_element_present(*LoginPageLocators.REG_BUTTON), "Items not found"
