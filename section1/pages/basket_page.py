from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def in_basket_no_products(self):
        assert self.browser.find_element(
            *BasketPageLocators.COUNT_PRODUCTS_IN_BASKET).text == "Your basket is empty. Continue shopping", "Корзина не пуста"
