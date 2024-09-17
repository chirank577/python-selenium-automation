from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')



@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.sc-e487bf3b-1.fSHTpu").click()


@when('click on sign in logo')
def sign_in_logo(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()



@when ('click Sign In')
def click_sign_in_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(2)

@when('search for a {item}')
def search_products(context, item):
    context.driver.find_element(By.XPATH,"//input[@data-test='@web/Search/SearchInput']").send_keys(item)
    sleep(5)
#search button=> click
    context.driver.find_element(By.CSS_SELECTOR, "button.sc-1c2974c-3.bsiIIZ").click()
    sleep(10)



