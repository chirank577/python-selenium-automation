
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target Help page')
def open_target_help_page(context):
    context.app.Target_select.open_target_help_page()
    sleep(5)

@when('Click on Target Help at the bottom of the page')
def target_help_click(context):
    context.app.Target_select.target_help_click()
    sleep(10)

@when('scroll down on Holiday Help')
def click_on_Order_purchase(context):
    context.app.Target_select.dd_on_Holiday_help()

@when('Click on Holiday Help under holiday help')
def click_on_print_receipt(context):
    context.app.Target_select.click_on_Holiday_help()
    sleep(4)

# @then('Verify Holiday Help page is open')
# def verify_Holiday_Help(context):
#     context.app.Target_select.verify_Holiday_help()

@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.Target_select.select_topic(option)

# @then('Verify {header} text is shown')
# def verify_Target_Account_opened(context):
#     context.app.Target_select.verify_Target_Account_opened()

@then('verify {expected_header_text} page is open')
def verify_holiday_help_page_opened(context, expected_header_text):
    context.app.Target_select.verify_header(expected_header_text)




