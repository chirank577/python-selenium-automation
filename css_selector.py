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
