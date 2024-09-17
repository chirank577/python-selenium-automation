from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then ('Verify Sign In form opened')
def Sig_in_opened(context):
    actual_result=context.driver.find_element(By.XPATH, "//h1[contains(@class, 'sc-fe064f5c-0')]").text
    expected_result= 'Sign into your Target account'
    assert actual_result== expected_result, f' expected : {expected_result} but received : {actual_result}.'