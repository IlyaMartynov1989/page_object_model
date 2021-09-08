import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators, BasketLocators


class Basket(BasePage):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_to_basket(self):
        buttom = self.browser.find_element(*BasketLocators.ADD_PRODUCT)
        buttom.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_data_by_card_product(self):
        text = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1").text
        price = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color").text
        return text, price

    def get_data_by_basket(self):
        text = self.browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong").text
        price = self.browser.find_element(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong").text
        return text, price