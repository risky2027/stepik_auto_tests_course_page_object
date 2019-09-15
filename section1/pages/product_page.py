from .base_page import BasePage
from .locators import BookPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*BookPageLocators.BUTTON_BASKET)
        link.click()

    def check_names_products(self):
        product_name_before = self.browser.find_element(*BookPageLocators.NAME_PRODUCT_BEFORE).text
        product_name_after = self.browser.find_element(*BookPageLocators.NAME_PRODUCT_AFTER).text
        assert product_name_before == product_name_after, "Названия продуктов разные"

    def check_prices_products(self):
        product_price_before = self.browser.find_element(*BookPageLocators.PRICE_PRODUCT_BEFORE).text
        product_price_after = self.browser.find_element(*BookPageLocators.PRICE_PRODUCT_AFTER).text
        assert product_price_before == product_price_after, "Цены продуктов разные"
