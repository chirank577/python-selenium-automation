from importlib.metadata import pass_none

from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SearchResultPage(Page):
    Search_result_header = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
    VIEW_CART = (By.XPATH, "//button[@data-test='orderPickupButton']")
    def verify_result(self, Product):
        self.verify_partial_text(Product, *self.Search_result_header)

    def Product_is_added_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def Click_on_view_cart_and_check_out(self):
        self.click(*self.VIEW_CART)

