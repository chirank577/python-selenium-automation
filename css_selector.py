from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(10)
#css selecctor
driver.find_element(By.CSS_SELECTOR, "a#nav-link-accountList.nav-a.nav-a-2.nav-progressive-attribute").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.a-button-text").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name.a-input-text")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.a-spacing-micro.auth-required-field.auth-require-claim-validation")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[aria-describedby='ap_password_context_message_section']")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "[autocomplete='new-password'][aria-describedby='ap_password_check_context_message_section']")
driver.find_element(By.XPATH, "//input[@aria-describedby='legalTextRow']")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
sleep(2)
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
sleep(2)
#
# lana's lesson 2 code'
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.amazon.com/')
#
# # Locate element:
# # driver.find_element() # By. / value
# # Locate by ID:
# driver.find_element(By.ID, 'twotabsearchtextbox')
# driver.find_element(By.ID, 'nav-logo-sprites')
#
# # By Xpath, using 1 attribute
# driver.find_element(By.XPATH, "//img[@alt='Shop Studio Pro headphones']")
# driver.find_element(By.XPATH, "//input[@name='field-keywords']")
# driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
# # By Xpath, multiple attributes
# driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")
#
# # By Xpath, text:
# driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# driver.find_element(By.XPATH, '//a[text()="Best Sellers"]')
# # By Xpath, text and attributes:
# driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
#
# # By attributes or text only, any tag
# driver.find_element(By.XPATH, "//*[@name='field-keywords']")
# driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")
#
# # By attributes, parent node => child
# driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")
#  30 changes: 30 additions & 0 deletions30
# target_search.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,30 @@
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# driver.get('https://www.target.com/')
#
# # Search field => enter tea
# driver.find_element(By.ID, 'search').send_keys('tea')
#
# # Search button => click
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# sleep(6)  # wait for search results page to load
#
# # Verification
# actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
# expected_result = 'tea'
#
# assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
# print('Test case passed')
#
# driver.quit()


#
# #lana code lesson 3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# # driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.amazon.com/')
#
# # By CSS, by ID, use #:
# driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# # Same as =>
# driver.find_element(By.ID, "twotabsearchtextbox")  # Note, By.ID is preferred if you only use ID
#
# # By CSS, by class, use .
# driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute")
# driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
# # By CSS, by tag & class(es)
# driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
# # By CSS, tag & ID & class
# driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")
#
# # By CSS, attributes, use []:
# driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
# driver.find_element(By.CSS_SELECTOR, ".nav-input[tabindex='0'][placeholder='Search Amazon']")
#
# # By CSS, attribute, partial match:
# driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
# driver.find_element(By.CSS_SELECTOR, "[class*='search']")
# driver.find_element(By.CSS_SELECTOR, "[id*='search']")
#
# # By CSS, from parent => to child, separate by space:
# driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
# driver.find_element(By.CSS_SELECTOR, ".a-box-inner #legalTextRow [href*='privacy']")



# lan's code lesson 4
# from selenium.webdriver.common.by import By
# from behave import given, when, then
#
#
# @then('Verify Cart Empty message shown')
# def verify_cart_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
#     assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
#  42 changes: 42 additions & 0 deletions42
# features/steps/main_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,42 @@
# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('Click on cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#
#
# @when('Search for {item}')
# def search_product(context, item):
#     # print(item)
#     # Search field => enter tea
#     context.driver.find_element(By.ID, 'search').send_keys(item)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)  # wait for search results page to load
#
#
# @then('Verify header has {expected_amount} links')
# def verify_header_links(context, expected_amount):
#     expected_amount = int(expected_amount) # '6' => 6
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
#     assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
#
#
# @then('Verify header is shown')
# def verify_header(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")
#
#
# # Example with multiple variables:
# # @when('Login as {username} and {pw}')
# # def search_product(context, username, pw):
# #     context.driver.find_element(By.ID, 'username').send_keys(username)
# #     context.driver.find_element(By.ID, 'password').send_keys(pw)
#  32 changes: 0 additions & 32 deletions32
# features/steps/product_search.py
# This file was deleted.
#
#  9 changes: 9 additions & 0 deletions9
# features/steps/search_results_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,9 @@
# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert product in actual_result, f'Expected {product}, got actual {actual_result}'
#  24 changes: 0 additions & 24 deletions24
# features/steps/target_steps.py
# This file was deleted.
#
#  6 changes: 6 additions & 0 deletions6
# features/tests/cart.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,6 @@
# Feature: Cart tests
#
#   Scenario: User can see Cart Empty message
#     Given Open target main page
#     When Click on cart icon
#     Then Verify Cart Empty message shown
#  10 changes: 10 additions & 0 deletions10
# features/tests/main_page_ui_tests.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,10 @@
# Feature: Tests for main page UI
#
#   Scenario: Verify header in shown
#     Given Open Target main page
#     Then Verify header is shown
#
#   Scenario: Verify header has correct amount links
#     Given Open Target main page
#     Then Verify header is shown
#     And Verify header has 6 links
#  7 changes: 0 additions & 7 deletions7
# features/tests/product_search.feature
# This file was deleted.
#
#  26 changes: 16 additions & 10 deletions26
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -1,17 +1,23 @@
# # Created by lana at 9/5/24
# Feature: Tests for Target Search functionality
#
#   Scenario: User can search for a product
#   Scenario: User can search for coffee
#     Given Open target main page
#     When Search for a product
#     Then Verify that correct search results shown
#     When Search for coffee
#     Then Verify that correct search results shown for coffee
#
#   Scenario: User can search for a product2
#   Scenario: User can search for tea
#     Given Open target main page
# #    When Search for a product
# #    Then Verify that correct search results shown
#     When Search for tea
#     Then Verify that correct search results shown for tea
#
# #  Scenario: User can see Cart Empty message
# #    Given Open target main page
# #    When Click on cart icon
# #    Then Verify cart Empty message shown
#   Scenario Outline: User can search for product
#     Given Open target main page
#     When Search for <search_word>
#     Then Verify that correct search results shown for <search_result>
#     Examples:
#     |search_word  |search_result |
#     |coffee       |coffee        |
#     |tea          |tea           |
#     |mug          |mug           |
#     |sugar        |sugar         |

#lesson 5 lana's code
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @@ -13,6 +14,7 @@ def browser_init(context):
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, timeout=10)
#
#
# def before_scenario(context, scenario):
#  21 changes: 21 additions & 0 deletions21
# features/steps/cart_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -1,9 +1,30 @@
# from selenium.webdriver.common.by import By
# from behave import given, when, then
#
# CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
# CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
#
#
# @when('Open cart page')
# def open_cart(context):
#     context.driver.get('https://www.target.com/cart')
#
#
# @then('Verify Cart Empty message shown')
# def verify_cart_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
#     assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
#
#
# @then('Verify cart has correct product')
# def verify_product_name(context):
#     actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
#     print(f'Actual product in cart name: {actual_name}')
#     assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
#
#
# @then('Verify cart has {amount} item(s)')
# def verify_cart_items(context, amount):
#     cart_summary = context.driver.find_element(*CART_SUMMARY).text
#     assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
#   9 changes: 1 addition & 8 deletions9
# features/steps/main_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -20,7 +20,7 @@ def search_product(context, item):
#     context.driver.find_element(By.ID, 'search').send_keys(item)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)  # wait for search results page to load
#     sleep(8)  # wait for search results page to load
#
#
# @then('Verify header has {expected_amount} links')
# @@ -33,10 +33,3 @@ def verify_header_links(context, expected_amount):
# @then('Verify header is shown')
# def verify_header(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")
#
#
# # Example with multiple variables:
# # @when('Login as {username} and {pw}')
# # def search_product(context, username, pw):
# #     context.driver.find_element(By.ID, 'username').send_keys(username)
# #     context.driver.find_element(By.ID, 'password').send_keys(pw)
#  35 changes: 35 additions & 0 deletions35
# features/steps/product_details_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,35 @@
# from selenium.webdriver.common.by import By
# from behave import given, then
# from time import sleep
#
#
# COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
# SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
#
#
# @given('Open target product {product_id} page')
# def open_target(context, product_id):
#     context.driver.get(f'https://www.target.com/p/{product_id}')
#     sleep(8)
#
#
# @then('Verify user can click through colors')
# def click_and_verify_colors(context):
#     expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
#     print(colors)
#
#     for color in colors:
#         print(color)
#         color.click()
#
#         selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
#         print('Current color text', selected_color)
#
#         selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
#         actual_colors.append(selected_color)
#         print('actual_colors list: ', actual_colors)
#
#     assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
#  28 changes: 28 additions & 0 deletions28
# features/steps/search_results_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -1,8 +1,36 @@
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from behave import given, when, then
# from time import sleep
#
#
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
#
#
#
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
#     context.driver.wait.until(
#         EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
#         message='Side navigation product name not visible'
#     )
#
#
# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print(f'Product stored: {context.product_name}')
#
#
# @when('Confirm Add to Cart button from side navigation')
# def side_nav_click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
#     sleep(3)
#
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#  5 changes: 5 additions & 0 deletions5
# features/tests/product_details.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,5 @@
# Feature: Tests for product page
#
#   Scenario: User can select colors
#     Given Open target product A-54551690 page
#     Then Verify user can click through colors
#   10 changes: 10 additions & 0 deletions10
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -21,3 +21,13 @@ Feature: Tests for Target Search functionality
#     |tea          |tea           |
#     |mug          |mug           |
#     |sugar        |sugar         |
#
#   Scenario: User can add a product to cart
#     Given Open target main page
#     When Search for mug
#     And Click on Add to Cart button
#     And Store product name
#     And Confirm Add to Cart button from side navigation
#     And Open cart page
#     Then Verify cart has 1 item(s)
#     And Verify cart has correct product
#   10 changes: 8 additions & 2 deletions10
# sample_script.py
# Original file line number	Diff line number	Diff line change
# @@ -2,6 +2,8 @@
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# # get the path to the ChromeDriver executable
# @@ -11,6 +13,8 @@
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# # driver.implicitly_wait(4)
# wait = WebDriverWait(driver, timeout=10)
#
# # open the url
# driver.get('https://www.google.com/')
# @@ -21,10 +25,12 @@
# search.send_keys('Car')
#
# # wait for 4 sec
# sleep(4)
# # sleep(4)
# search_btn = (By.NAME, 'btnK')
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
# wait.until(EC.element_to_be_clickable(search_btn), message='Search button not clickable').click()  # => (By.smth, "value")
# driver.find_element(*search_btn).click() # => 2: By..smth / "value"
#
# # verify search results
# assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"

#LESSON 6 CODE
# from pages.base_page import Page
# from pages.header import Header
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
#
#
# class Application:
#
#     def __init__(self, driver):
#         self.page = Page(driver)
#         self.main_page = MainPage(driver)
#         self.header = Header(driver)
#         self.search_results_page = SearchResultsPage(driver)
#   3 changes: 3 additions & 0 deletions3
# features/environment.py
# Original file line number	Diff line number	Diff line change
# @@ -3,6 +3,8 @@
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
#
# from app.application import Application
#
#
# def browser_init(context):
#     """
# @@ -15,6 +17,7 @@ def browser_init(context):
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, timeout=10)
#     context.app = Application(context.driver)
#
#
# def before_scenario(context, scenario):
#   10 changes: 2 additions & 8 deletions10
# features/steps/main_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -1,11 +1,10 @@
# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')
#     context.app.main_page.open_main()
#
#
# @when('Click on cart icon')
# @@ -15,12 +14,7 @@ def click_cart(context):
#
# @when('Search for {item}')
# def search_product(context, item):
#     # print(item)
#     # Search field => enter tea
#     context.driver.find_element(By.ID, 'search').send_keys(item)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(8)  # wait for search results page to load
#     context.app.header.search_product(item)
#
#
# @then('Verify header has {expected_amount} links')
#   23 changes: 20 additions & 3 deletions23
# features/steps/search_results_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -7,7 +7,9 @@
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
#
# LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
# PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
#
#
# @when('Click on Add to Cart button')
# @@ -33,5 +35,20 @@ def side_nav_click_add_to_cart(context):
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert product in actual_result, f'Expected {product}, got actual {actual_result}'
#     context.app.search_results_page.verify_results(product)
#
#
# @then('Verify that every product has a name and an image')
# def verify_products_name_img(context):
#     # To see ALL listings (comment out if you only check top ones):
#     context.driver.execute_script("window.scrollBy(0,2000)", "")
#     sleep(4)
#     context.driver.execute_script("window.scrollBy(0,2000)", "")
#
#     all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
#
#     for product in all_products:
#         title = product.find_element(*PRODUCT_TITLE).text
#         assert title, 'Product title not shown'
#         print(title)
#         product.find_element(*PRODUCT_IMG)
#   7 changes: 6 additions & 1 deletion7
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -30,4 +30,9 @@ Feature: Tests for Target Search functionality
#     And Confirm Add to Cart button from side navigation
#     And Open cart page
#     Then Verify cart has 1 item(s)
#     And Verify cart has correct product
#     And Verify cart has correct product
#
#   Scenario: Verify that user can see product names and images
#     Given Open target main page
#     When Search for AirPods (3rd Generation)
#     Then Verify that every product has a name and an image
#  Empty file added0
# pages/__init__.py
# Empty file.
#  19 changes: 19 additions & 0 deletions19
# pages/base_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,19 @@
# class Page:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open(self, url):
#         self.driver.get(url)
#
#     def find_element(self, *locator):
#         return self.driver.find_element(*locator)
#
#     def find_elements(self, *locator):
#         return self.driver.find_elements(*locator)
#
#     def click(self, *locator):
#         self.driver.find_element(*locator).click()
#
#     def input_text(self, text, *locator):
#         self.driver.find_element(*locator).send_keys(text)
#  13 changes: 13 additions & 0 deletions13
# pages/header.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,13 @@
# from selenium.webdriver.common.by import By
# from time import sleep
#
# from pages.base_page import Page
#
# class Header(Page):
#     SEARCH_FIELD = (By.ID, 'search')
#     SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
#
#     def search_product(self, item):
#         self.input_text(item, *self.SEARCH_FIELD)
#         self.click(*self.SEARCH_BTN)
#         sleep(6) # wait for search results page to load
#  7 changes: 7 additions & 0 deletions7
# pages/main_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,7 @@
# from pages.base_page import Page
#
#
# class MainPage(Page):
#
#     def open_main(self):
#         self.open('https://www.target.com/')
#  10 changes: 10 additions & 0 deletions10
# pages/search_results_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,10 @@
# from selenium.webdriver.common.by import By
#
# from pages.base_page import Page
#
# class SearchResultsPage(Page):
#     SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
#
#     def verify_results(self, product):
#         actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
#         assert product in actual_result, f'Expected {product}, got actual {actual_result}'

LESSON 7 Lana's code
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# # driver.implicitly_wait(4)
# wait = WebDriverWait(driver, timeout=10)
#
# # open the url
# driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
# sleep(2)
#
# links = driver.find_elements(By.CSS_SELECTOR, '#zg_header a')
# print(links)
#
# for i in range(len(links)):
#     links = driver.find_elements(By.CSS_SELECTOR, '#zg_header a')
#     links[i].click()
#     sleep(2)
#   2 changes: 2 additions & 0 deletions2
# app/application.py
# Original file line number	Diff line number	Diff line change
# @@ -1,4 +1,5 @@
# from pages.base_page import Page
# from pages.cart_page import CartPage
# from pages.header import Header
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
# @@ -8,6 +9,7 @@ class Application:
#
#     def __init__(self, driver):
#         self.page = Page(driver)
#         self.cart_page = CartPage(driver)
#         self.main_page = MainPage(driver)
#         self.header = Header(driver)
#         self.search_results_page = SearchResultsPage(driver)
#   4 changes: 1 addition & 3 deletions4
# features/steps/cart_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -12,9 +12,7 @@ def open_cart(context):
#
# @then('Verify Cart Empty message shown')
# def verify_cart_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
#     assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
#     context.app.cart_page.verify_cart_empty()
#
#
# @then('Verify cart has correct product')
#   2 changes: 1 addition & 1 deletion2
# features/steps/main_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -9,7 +9,7 @@ def open_main(context):
#
# @when('Click on cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#     context.app.header.click_cart()
#
#
# @when('Search for {item}')
#   5 changes: 5 additions & 0 deletions5
# features/steps/search_results_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -38,6 +38,11 @@ def verify_results(context, product):
#     context.app.search_results_page.verify_results(product)
#
#
# @then('Verify product {product} in URL')
# def verify_results_url(context, product):
#     context.app.search_results_page.verify_results_url(product)
#
#
# @then('Verify that every product has a name and an image')
# def verify_products_name_img(context):
#     # To see ALL listings (comment out if you only check top ones):
#   1 change: 1 addition & 0 deletions1
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -5,6 +5,7 @@ Feature: Tests for Target Search functionality
#     Given Open target main page
#     When Search for coffee
#     Then Verify that correct search results shown for coffee
#     Then Verify product coffee in URL
#
#   Scenario: User can search for tea
#     Given Open target main page
#   49 changes: 49 additions & 0 deletions49
# pages/base_page.py
# Original file line number	Diff line number	Diff line change
# @@ -1,7 +1,12 @@
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class Page:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, timeout=10)
#
#     def open(self, url):
#         self.driver.get(url)
# @@ -12,8 +17,52 @@ def find_element(self, *locator):
#     def find_elements(self, *locator):
#         return self.driver.find_elements(*locator)
#
#     def get_text(self, *locator):
#         return self.find_element(*locator).text
#
#     def click(self, *locator):
#         self.driver.find_element(*locator).click()
#
#     def input_text(self, text, *locator):
#         self.driver.find_element(*locator).send_keys(text)
#
#     def wait_to_be_clickable(self, *locator):
#         self.wait.until(
#             EC.element_to_be_clickable(locator),
#             message=f'Element by {locator} not clickable'
#         )
#
#     def wait_to_be_clickable_click(self, *locator):
#         self.wait.until(
#             EC.element_to_be_clickable(locator),
#             message=f'Element by {locator} not clickable'
#         ).click()
#
#     def wait_for_element_to_appear(self, *locator):
#         self.wait.until(
#             EC.visibility_of_element_located(locator),
#             message=f'Element by {locator} did not appear'
#         )
#
#     def wait_for_element_to_disappear(self, *locator):
#         self.wait.until(
#             EC.invisibility_of_element_located(locator),
#             message=f'Element by {locator} still shown on the page'
#         )
#
#     def verify_text(self, expected_text, *locator):
#         actual_text = self.find_element(*locator).text
#         assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'
#
#     def verify_partial_text(self, expected_text, *locator):
#         actual_text = self.find_element(*locator).text
#         assert expected_text in actual_text, f'Expected {expected_text} not shown in actual {actual_text}'
#
#     def verify_url(self, expected_url):
#         current_url = self.driver.current_url
#         assert current_url == expected_url, f'Expected URL {expected_url} but got {current_url}'
#
#     def verify_partial_url(self, expected_partial_url):
#         current_url = self.driver.current_url
#         assert expected_partial_url in current_url, \
#             f'Expected partial URL {expected_partial_url} not in {current_url}'
#  9 changes: 9 additions & 0 deletions9
# pages/cart_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,9 @@
# from selenium.webdriver.common.by import By
#
# from pages.base_page import Page
#
# class CartPage(Page):
#     CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
#
#     def verify_cart_empty(self):
#         self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)
#   5 changes: 5 additions & 0 deletions5
# pages/header.py
# Original file line number	Diff line number	Diff line change
# @@ -4,10 +4,15 @@
# from pages.base_page import Page
#
# class Header(Page):
#     CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
#     SEARCH_FIELD = (By.ID, 'search')
#     SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
#
#     def search_product(self, item):
#         self.input_text(item, *self.SEARCH_FIELD)
#         self.click(*self.SEARCH_BTN)
#         sleep(6) # wait for search results page to load
#
#     def click_cart(self):
#         self.wait_to_be_clickable_click(*self.CART_BTN)
#         # self.driver.find_element(*self.CART_BTN).click()
#   6 changes: 4 additions & 2 deletions6
# pages/search_results_page.py
# Original file line number	Diff line number	Diff line change
# @@ -6,5 +6,7 @@ class SearchResultsPage(Page):
#     SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
#
#     def verify_results(self, product):
#         actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
#         assert product in actual_result, f'Expected {product}, got actual {actual_result}'
#         self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)
#
#     def verify_results_url(self, product):
#         self.verify_partial_url(product)

lesson 8
# from pages.header import Header
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
# from pages.target_app_page import TargetAppPage
#
#
# class Application:
# @@ -13,3 +14,4 @@ def __init__(self, driver):
#         self.main_page = MainPage(driver)
#         self.header = Header(driver)
#         self.search_results_page = SearchResultsPage(driver)
#         self.target_app_page = TargetAppPage(driver)
#   45 changes: 43 additions & 2 deletions45
# features/environment.py
# Original file line number	Diff line number	Diff line change
# @@ -2,18 +2,59 @@
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options

from app.application import Application

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

# def browser_init(context):
#
# def browser_init(context, scenario_name):
#     """
#     :param context: Behave context
#     """
#     driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='put your path to driver file here')
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'edge',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)
#     context.driver.wait = WebDriverWait(context.driver, timeout=10)
# @@ -22,7 +63,7 @@ def browser_init(context):
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)
#     browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#  37 changes: 37 additions & 0 deletions37
# features/steps/target_app_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,37 @@
# from behave import given, when, then
#
#
# @given('Open Target App page')
# def open_target_app(context):
#     context.app.target_app_page.open_target_app()
#
#
# @given('Store original window')
# def store_window(context):
#     context.original_window = context.app.target_app_page.get_current_window()
#     print('Original window: ', context.original_window)
#
#
# @when('Click Privacy Policy link')
# def click_pp_link(context):
#     context.app.target_app_page.click_pp_link()
#
#
# @when('Switch to new window')
# def switch_to_window(context):
#     context.app.target_app_page.switch_to_new_window()
#
#
# @then('Verify Privacy Policy page opened')
# def verify_pp_opened(context):
#     context.app.target_app_page.verify_pp_opened()
#
#
# @then('Close current page')
# def close_page(context):
#     context.app.target_app_page.close()
#
#
# @then('Return to original window')
# def switch_to_original(context):
#     context.app.target_app_page.switch_to_window_by_id(context.original_window)
#  10 changes: 10 additions & 0 deletions10
# features/tests/target_app_ui_tests.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,10 @@
# Feature: Tests for Target App page
#
#   Scenario: User is able to open Privacy Policy
#     Given Open Target App page
#     And Store original window
#     When Click Privacy Policy link
#     And Switch to new window
#     Then Verify Privacy Policy page opened
#     And Close current page
#     And Return to original window
#   16 changes: 16 additions & 0 deletions16
# pages/base_page.py
# Original file line number	Diff line number	Diff line change
# @@ -50,6 +50,22 @@ def wait_for_element_to_disappear(self, *locator):
#             message=f'Element by {locator} still shown on the page'
#         )
#
#     def get_current_window(self):
#         return self.driver.current_window_handle
#
#     def switch_to_new_window(self):
#         self.wait.until(EC.new_window_is_opened)
#         all_windows = self.driver.window_handles
#         print(f'Switching to window {all_windows[1]}')
#         self.driver.switch_to.window(all_windows[1])
#
#     def switch_to_window_by_id(self, window_id):
#         print(f'Switching to window {window_id}')
#         self.driver.switch_to.window(window_id)
#
#     def close(self):
#         self.driver.close()
#
#     def verify_text(self, expected_text, *locator):
#         actual_text = self.find_element(*locator).text
#         assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'
#  16 changes: 16 additions & 0 deletions16
# pages/target_app_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,16 @@
# from selenium.webdriver.common.by import By
#
# from pages.base_page import Page
#
#
# class TargetAppPage(Page):
#     PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")
#
#     def open_target_app(self):
#         self.open('https://www.target.com/c/target-app/')
#
#     def click_pp_link(self):
#         self.wait_to_be_clickable_click(*self.PP_LINK)
#
#     def verify_pp_opened(self):
#         self.verify_partial_url('target-privacy-policy/')


Lesson 9
# from pages.base_page import Page
# from pages.cart_page import CartPage
# from pages.header import Header
# from pages.help_page import HelpPage
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
# from pages.target_app_page import TargetAppPage
# @@ -13,5 +14,6 @@ def __init__(self, driver):
#         self.cart_page = CartPage(driver)
#         self.main_page = MainPage(driver)
#         self.header = Header(driver)
#         self.help_page = HelpPage(driver)
#         self.search_results_page = SearchResultsPage(driver)
#         self.target_app_page = TargetAppPage(driver)
#  25 changes: 25 additions & 0 deletions25
# features/steps/help_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,25 @@
# from behave import given, when, then
#
#
# @given('Open Help page for Returns')
# def click_cart(context):
#     context.app.help_page.open_help_returns()
#
#
# @when('Select Help topic {option}')
# def select_topic(context, option):
#     context.app.help_page.select_topic(option)
#
#
# # @then('Verify help Returns page opened')
# # def verify_returns_opened(context):
# #     context.app.help_page.verify_returns_opened()
# #
# #
# # @then('Verify help Current promotions page opened')
# # def verify_promotions_opened(context):
# #     context.app.help_page.verify_promotions_opened()
#
# @then('Verify help {expected_header_text} page opened')
# def verify_returns_opened(context, expected_header_text):
#     context.app.help_page.verify_header(expected_header_text)
#   10 changes: 10 additions & 0 deletions10
# features/steps/search_results_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -33,6 +33,16 @@ def side_nav_click_add_to_cart(context):
#     sleep(3)
#
#
# @when('Hover favorites icon')
# def hover_favorites(context):
#     context.app.search_results_page.hover_favorites()
#
#
# @then('Favorites tooltip is shown')
# def verify_favorites(context):
#     context.app.search_results_page.verify_favorites()
#
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     context.app.search_results_page.verify_results(product)
#  13 changes: 13 additions & 0 deletions13
# features/tests/help_tests.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,13 @@
# Feature: Tests for Help pages
#
#   Scenario: User can select Help topic Promotions & Coupons
#     Given Open Help page for Returns
#     Then Verify help Returns page opened
#     When Select Help topic Promotions & Coupons
#     Then Verify help Current promotions page opened
#
#   Scenario: User can select Help topic About Target Circle
#     Given Open Help page for Returns
#     Then Verify help Returns page opened
#     When Select Help topic Target Circle™
#     Then Verify help About Target Circle page opened
#   6 changes: 6 additions & 0 deletions6
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -37,3 +37,9 @@ Feature: Tests for Target Search functionality
#     Given Open target main page
#     When Search for AirPods (3rd Generation)
#     Then Verify that every product has a name and an image
#
#   Scenario: User can see favorites tooltip for search results
#     Given Open Target main page
#     When Search for tea
#     And Hover favorites icon
#     Then Favorites tooltip is shown
#  28 changes: 28 additions & 0 deletions28
# frames.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,28 @@
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# # init driver
# driver_path = ChromeDriverManager().install()
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
#
# driver.implicitly_wait(4)
#
# # open the url
# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')
#
# # Switch to frame 1
# driver.switch_to.frame('iframeResult')
#
# # Switch to frame 2
# frame2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
# driver.switch_to.frame(frame2)
#
# menu = driver.find_element(By.CSS_SELECTOR, '.tnb-menu-btn')
# print(menu.get_attribute('title'))
#
# assert menu.get_attribute('title') == 'Menu', f"Title is {menu.get_attribute('title')} instead of Menu"
#
# driver.quit()
#   2 changes: 1 addition & 1 deletion2
# pages/header.py
# Original file line number	Diff line number	Diff line change
# @@ -11,7 +11,7 @@ class Header(Page):
#     def search_product(self, item):
#         self.input_text(item, *self.SEARCH_FIELD)
#         self.click(*self.SEARCH_BTN)
#         sleep(6) # wait for search results page to load
#         sleep(8) # wait for search results page to load
#
#     def click_cart(self):
#         self.wait_to_be_clickable_click(*self.CART_BTN)
#  36 changes: 36 additions & 0 deletions36
# pages/help_page.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,36 @@
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# from pages.base_page import Page
#
#
# class HelpPage(Page):
#     # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
#     # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
#     HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
#     TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
#
#     # Dynamic locator
#     def _get_locator(self, expected_header_text):
#         # (By.XPATH, "//h1[text()=' Returns']")
#         # (By.XPATH, "//h1[text()=' {expected_header_text}']")
#         # (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Current promotions']")
#         return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', expected_header_text)]
#
#     def open_help_returns(self):
#         self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
#
#     def select_topic(self, option):
#         dd = self.find_element(*self.TOPIC_SELECTION)
#         select = Select(dd)
#         select.select_by_value(option)
#
#     def verify_header(self, expected_header_text):
#         header_locator = self._get_locator(expected_header_text)
#         self.wait_for_element_to_appear(*header_locator)
#
#     # def verify_returns_opened(self):
#     #     self.wait_for_element_to_appear(*self.HEADER_RETURNS)
#     #
#     # def verify_promotions_opened(self):
#     #     self.wait_for_element_to_appear(*self.HEADER_PROMOTIONS)
#  13 changes: 13 additions & 0 deletions13
# pages/search_results_page.py
# Original file line number	Diff line number	Diff line change
# @@ -1,9 +1,22 @@
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# from pages.base_page import Page
#
# class SearchResultsPage(Page):
#     SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
#     HEART_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
#     FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")
#
#     def hover_favorites(self):
#         heart_icon = self.find_element(*self.HEART_ICON)
#
#         actions = ActionChains(self.driver)
#         actions.move_to_element(heart_icon)
#         actions.perform()
#
#     def verify_favorites(self):
#         self.wait_for_element_to_appear(*self.FAV_TOOLTIP)
#
#     def verify_results(self, product):
#         self.verify_partial_text(product, *self.SEARCH_RESULTS_HEADER)

Lesson 10
# from selenium.webdriver.chrome.options import Options
#
# from app.application import Application
# from support.logger import logger
#
# # Command to run tests with Allure & Behave:
# # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature
# @@ -62,17 +63,20 @@ def browser_init(context, scenario_name):
#
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     # print('\nStarted scenario: ', scenario.name)
#     logger.info(f'Started scenario: {scenario.name}')
#     browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#     # print('\nStarted step: ', step)
#     logger.info(f'Started step: {step}')
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#         # print('\nStep failed: ', step)
#         logger.error(f'Step failed: {step}')
#
#
# def after_scenario(context, feature):
#  1 change: 1 addition & 0 deletions1
# features/tests/help_tests.feature
# Original file line number	Diff line number	Diff line change
# @@ -1,3 +1,4 @@
# @smoke
# Feature: Tests for Help pages
#
#   Scenario: User can select Help topic Promotions & Coupons
#  1 change: 1 addition & 0 deletions1
# features/tests/main_page_ui_tests.feature
# Original file line number	Diff line number	Diff line change
# @@ -1,5 +1,6 @@
# Feature: Tests for main page UI
#
#   @smoke
#   Scenario: Verify header in shown
#     Given Open Target main page
#     Then Verify header is shown
#  1 change: 1 addition & 0 deletions1
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -1,6 +1,7 @@
# # Created by lana at 9/5/24
# Feature: Tests for Target Search functionality
#
#   @smoke @safari_only
#   Scenario: User can search for coffee
#     Given Open target main page
#     When Search for coffee
#   7 changes: 7 additions & 0 deletions7
# pages/base_page.py
# Original file line number	Diff line number	Diff line change
# @@ -1,6 +1,8 @@
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# from support.logger import logger
#
#
# class Page:
#
# @@ -9,21 +11,26 @@ def __init__(self, driver):
#         self.wait = WebDriverWait(self.driver, timeout=10)
#
#     def open(self, url):
#         logger.info(f'Opening page {url}')
#         self.driver.get(url)
#
#     def find_element(self, *locator):
#         logger.info(f'Searching for element by {locator}')
#         return self.driver.find_element(*locator)
#
#     def find_elements(self, *locator):
#         logger.info(f'Searching for elements by {locator}')
#         return self.driver.find_elements(*locator)
#
#     def get_text(self, *locator):
#         return self.find_element(*locator).text
#
#     def click(self, *locator):
#         logger.info(f'Clicking on element {locator}')
#         self.driver.find_element(*locator).click()
#
#     def input_text(self, text, *locator):
#         logger.info(f'Inputting text for element {locator}')
#         self.driver.find_element(*locator).send_keys(text)
#
#     def wait_to_be_clickable(self, *locator):
#  Empty file added0
# support/__init__.py
# Empty file.
#  17 changes: 17 additions & 0 deletions17
# support/logger.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,17 @@
# import logging
#
# logger = logging.getLogger(__name__)
# # Determine which log messages are actually written to the log file.
# # logging.DEBUG will capture and log messages at all levels, including DEBUG, INFO, WARNING, ERROR, and CRITICAL.
# logger.setLevel(logging.DEBUG)
#
# # FileHandler is an object that defines how log messages should be written to a file
# # Create a file handler that will write log messages to a file named 'test_automation.log'
# handler = logging.FileHandler('./test_automation.log')
# handler.setLevel(logging.DEBUG)
#
# # Define the format for log messages, including timestamp, logger name, log level, and the actual message
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

