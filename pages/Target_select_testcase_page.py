from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class TargetSelectTestCase(Page):
    HELP_BUTTON=(By.XPATH, "//*[text()='Target Help']")
    # TARGET_ACCOUNT=(By.XPATH, "//a[contains(text(), 'Target Account')]")
    Help_Holiday = (By.CSS_SELECTOR, "li.closed div[class*='hitarea']:nth-of-type(1)")
    CLICK_HOLIDAY_HELP= (By.CSS_SELECTOR, "a[title*='Holiday Help']")
    TOPIC_SELECTION= (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    HEADER_ORDER_PURCHASE= (By.XPATH, "//h1[text()=' Holiday Help']")
    TARGET_ACCOUNT_TEXT= (By.XPATH, "//h2[text()='Target Account']")
    HEADER_TEXT= (By.XPATH, "//h1[text()=' {SUBSTRING}']")

    def _get_locator(self, expected_header_text):
        return [self.HEADER_TEXT[0], self.HEADER_TEXT[1].replace('{SUBSTRING}', expected_header_text)]



    def open_target_help_page(self):
        self.open('https://help.target.com/help')


    def target_help_click(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(*self.HELP_BUTTON)


    def dd_on_Holiday_help(self):
        self.click(*self.Help_Holiday)

    def click_on_Holiday_help(self):
        self.wait_to_be_clickable_click(*self.CLICK_HOLIDAY_HELP)

    # def verify_Holiday_help(self):
    #     self.verify_text('Holiday Help',*self.HEADER_ORDER_PURCHASE)

    def select_topic(self, option):
        dd= self.find_element(*self.TOPIC_SELECTION)
        select= Select(dd)
        select.select_by_value(option)

    # def verify_Target_Account_opened(self):
    #     self.verify_text('Target Account',*self.TARGET_ACCOUNT_TEXT)

    def verify_header(self, expected_header_text):
        header=self._get_locator(expected_header_text)
        self.wait_for_element_to_appear(*header)

