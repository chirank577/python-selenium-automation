from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.sc-e487bf3b-1.fSHTpu").click()
    sleep(5)

@then ('Your cart is empty message is shown')
def empty_msg(context):
    actual_result= context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 dtCtuk']").text
    assert actual_result == "Your cart is empty"
    sleep(5)
    print(actual_result)



@when('click on sign in logo')
def sign_in_logo(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(5)

@when ('click Sign In')
def click_sign_in_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(2)
@then ('Verify Sign In form opened')
def Sig_in_opened(context):
    actual_result=context.driver.find_element(By.XPATH, "//h1[contains(@class, 'sc-fe064f5c-0')]").text
    print(actual_result)