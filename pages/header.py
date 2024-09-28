from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    search_field= (By.XPATH,"//input[@data-test='@web/Search/SearchInput']")
    search_btn= (By.CSS_SELECTOR, "button.sc-1c2974c-3.bsiIIZ")
    ADD_CART_BTN= (By.CSS_SELECTOR, "div.sc-e487bf3b-1.fSHTpu")

    CLICK_SIGN_IN_MAIN_PAGE= (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    CLICK_SIGNIN=(By.XPATH, "//a[@data-test='accountNav-signIn']")
    def search_product(self, Product):
        self.input_text(Product, *self.search_field)
        self.click(*self.search_btn)
        sleep(15)

    def click_cart_btn(self):
        self.click(*self.ADD_CART_BTN)

    def click_sign_in_on_main_page(self):
        self.click(*self.CLICK_SIGN_IN_MAIN_PAGE)
        self.click(*self.CLICK_SIGNIN)

    VERIFY_USER_NAME_POST_LOGIN= (By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3")


    def VERIFY_USER_CAN_SIGN_IN_WITH_VALID_ID(self):
        self.verify_partial_text('Chiranjivi', *self.VERIFY_USER_NAME_POST_LOGIN)

