from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartVerification(Page):

    Verify_cart_is_empty=(By.CSS_SELECTOR, "[class='sc-fe064f5c-0 dtCtuk']")
    VERIFY_CART_HAS_PRODUCT= (By.CSS_SELECTOR, "span.sc-93ec7147-3.fUVkzh")

    def cart_empty(self):
        self.verify_text('Your cart is empty', *self.Verify_cart_is_empty)

    def Verify_cart_has_product_or_total_price(self, Item):
        self.verify_partial_text(Item,*self.VERIFY_CART_HAS_PRODUCT)


