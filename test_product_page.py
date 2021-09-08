from time import sleep

from .pages.main_page import MainPage
from .pages.product_page import Basket


def test_adding_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()

    basket = Basket(browser, browser.current_url)
    basket.add_to_basket()

    basket.solve_quiz_and_get_code()

    ex_text, ex_price = basket.get_data_by_card_product()
    text, price = basket.get_data_by_basket()

    assert ex_text==text, 'Наименование товара не совпало'
    assert ex_price == price, 'Стоимость товара не совпало'
