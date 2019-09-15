from pages.product_page import ProductPage
import time


def test_guest_can_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_name_before = product_page.get_name_product_before()
    product_price_before = product_page.get_price_product_before()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name_after = product_page.get_name_product_after()
    product_price_after = product_page.get_price_product_after()
    print(product_name_before, product_name_after)
    assert product_name_before == product_name_after and product_price_before == product_price_after, "Названия/цены не совпадают"
