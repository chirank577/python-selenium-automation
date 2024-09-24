from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

search_product= (By.CSS_SELECTOR,"input[data-test='@web/Search/SearchInput']")
click_search= (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
product_availability= (By.XPATH, "//div[@data-test='@web/site-top-of-funnel/ProductCardWrapper']")
product_title= (By.CSS_SELECTOR, "a[data-test='product-title']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
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

@when ('search for {product}')
def search_for_products(context, product):
    context.driver.find_element(*search_product).send_keys(product)
    sleep(1)
    context.driver.find_element(*click_search).click()
    sleep(4)

@then('Verify that every product on Target has a product name and product image')
def verify_product_shown(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    product_visible=context.driver.find_elements(*product_availability)
    # product_visible = context.driver.wait.until(EC.presence_of_all_elements_located(product_availability))
    for product in product_visible:
        title = product.find_element(*product_title).text
        assert title, f' product title now shown'
        print(title)
        product.find_element(By.CSS_SELECTOR, 'img')




