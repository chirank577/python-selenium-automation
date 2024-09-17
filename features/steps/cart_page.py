from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_CART_BTN= (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")


@then ('Your cart is empty message is shown')
def empty_msg(context):
    actual_result= context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 dtCtuk']").text
    expected_result = "Your cart is empty",
    assert actual_result== expected_result, f' Expected : {expected_result} but received : {actual_result}'
    sleep(2)


@when ('click add to cart button')
def add_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()
    sleep(2)

@when ('click on view cart & check out')
def click_view_cart(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "a.sc-ddc722c0-0.sc-3d5333d1-0.jKTcnK.hhYRAp").click()
    sleep(5)

@then ('verify cart has {Items} items or total price')
def verify_cart(context, Items):
    actual_result=context.driver.find_element(By.CSS_SELECTOR, "span.sc-93ec7147-3.fUVkzh").text
    assert Items in actual_result, f' expected result {Items} but got {actual_result}'
    sleep(5)