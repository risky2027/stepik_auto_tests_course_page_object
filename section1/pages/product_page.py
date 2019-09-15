from .base_page import BasePage
from .locators import BookPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*BookPageLocators.BUTTON_BASKET)
        link.click()

    def get_name_product_before(self):
        return self.browser.find_element(*BookPageLocators.NAME_PRODUCT_BEFORE).text

    def get_price_product_before(self):
        return self.browser.find_element(*BookPageLocators.PRICE_PRODUCT_BEFORE).text

    def get_name_product_after(self):
        return self.browser.find_element(*BookPageLocators.NAME_PRODUCT_AFTER).text

    def get_price_product_after(self):
        return self.browser.find_element(*BookPageLocators.PRICE_PRODUCT_AFTER).text
