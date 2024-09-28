from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_CART_BTN= (By.CSS_SELECTOR, "[id*='addToCartButton']")
VIEW_CART= (By.XPATH, "//button[@data-test='orderPickupButton']")

@then ('Your cart is empty message is shown')
def empty_msg(context):
    context.app.Cart_page.cart_empty()


@when ('click add to cart button')
def add_cart(context):
    context.app.search_result.Product_is_added_to_cart()
    sleep(5)

@when ('click on view cart & check out')
def click_view_cart(context):
    context.app.search_result.Click_on_view_cart_and_check_out()

    context.driver.find_element(By.CSS_SELECTOR, "a.sc-ddc722c0-0.sc-3d5333d1-0.jKTcnK.hhYRAp").click()
    sleep(5)

@then ('verify cart has {Item} items or total price')
def verify_cart(context, Item):
    context.app.Cart_page.Verify_cart_has_product_or_total_price(Item)