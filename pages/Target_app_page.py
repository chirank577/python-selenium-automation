from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class TargetAppPage(Page):
    Click_terms_condition= (By.CSS_SELECTOR,"a[aria-label*='terms & conditions']")
    condition_link= (By.XPATH, "//h3[contains(text(),'Your Use of This Website')]")

    def store_current_window(self):
         return self.get_current_window()

    def click_terms_condition(self):
        self.click(*self.Click_terms_condition)

    def switching_to_new_window(self):
        self.switch_to_window()


    def verify_condition_page_is_open(self):
        self.verify_partial_url('terms-conditions')

    def close_old_windows(self):
        self.close()

    def getback_to_orignal_window(self, id):
        self.Switch_to_original_window(id)



