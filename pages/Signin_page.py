from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    Sign_In_text_verification= (By.XPATH, "//h1[contains(@class, 'sc-fe064f5c-0')]")
    ENTER_EMAIL_ID= (By.ID, 'username')
    ENTER_PASSWORD= (By.ID, 'password')
    SING_IN_WITH_PSWD_BTN=(By.ID, 'login')
    def SIGN_IN_VERIFICATION(self):
        self.verify_text('Sign into your Target account', *self.Sign_In_text_verification)

    def Enter_email(self, email):
        self.input_text(email, *self.ENTER_EMAIL_ID)

    def Enter_password(self, password):
        self.input_text(password, *self.ENTER_PASSWORD)

    def Click_on_signin_with_pswd_btn(self):
        self.click(*self.SING_IN_WITH_PSWD_BTN)

    VERIFY_USER_NAME_POST_LOGIN = (By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3")
    CANNOT_FIND_ACCOUNT = (By.XPATH, "//div//div[contains(text(), 'We can')]")

    def VERIFY_USER_CAN_SIGN_IN_WITH_VALID_ID(self):
        self.verify_partial_text('Chiranjivi', *self.VERIFY_USER_NAME_POST_LOGIN)

    def Verify_user_cannot_signin(self):
        self.verify_text("We can't find your account.", *self.CANNOT_FIND_ACCOUNT)



