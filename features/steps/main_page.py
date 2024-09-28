from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#


@given('open target main page')
def open_target_main_page(context):
    context.app.main_page.open_main()



@when('click on cart icon')
def click_cart(context):
    context.app.header.click_cart_btn()


@when('click on sign in logo and sign in on account page')
def sign_in_logo(context):
    context.app.header.click_sign_in_on_main_page()


# @when ('click Sign In')
# def click_sign_in_menu(context):
#     context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
#     sleep(2)

@when('search for a {item}')
def search_products(context, item):
   context.app.header.search_product(item)


