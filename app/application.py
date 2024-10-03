from webbrowser import Chrome

from pages.Cart_page import CartVerification
from pages.Signin_page import  SignInPage
from pages.Target_app_page import TargetAppPage
from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.Target_select_testcase_page import TargetSelectTestCase


class Application:

    def __init__(self, driver):
        self.base_page= Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result= SearchResultPage(driver)
        self.Cart_page= CartVerification(driver)
        self.Signin_page= SignInPage(driver)
        self.Target_app_page= TargetAppPage(driver)
        self.Target_select= TargetSelectTestCase(driver)

