from pages.product_page import ProductPage
import time


def test_product_name_equal(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_name_before = product_page.get_name_product_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name_after = product_page.get_name_product_after()
    assert product_name_before == product_name_after, "Названия не совпадают"


def test_product_price_equal(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_price_before = product_page.get_price_product_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_price_after = product_page.get_price_product_after()
    assert product_price_before == product_price_after, "Цены не совпадают"
