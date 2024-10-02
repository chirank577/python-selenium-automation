from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Store original window')
def store_window(context):
    context.original_window = context.app.Target_app_page.store_current_window()
    print(context.original_window)
    sleep(2)

@when ('Click on Target terms and condition link')
def click_on_target_terms_and_condition_link(context):
    context.app.Target_app_page.click_terms_condition()
    sleep(2)

@when('switch to the newly opened window')
def switch_to_new_window(context):
    context.app.Target_app_page.switching_to_new_window()
    print(context.app.Target_app_page.store_current_window())


@then('Verify terms and condition page is opened')
def verify_terms_and_condition_page_is_opened(context):
    context.app.Target_app_page.verify_condition_page_is_open()

@then('close current window')
def close_page_and_verify_it_switched_back_to_old_page(context):
    context.app.Target_app_page.close_old_windows()
    sleep(3)

@then('return to original window')
def switch_back_to_original_window(context):
    context.app.Target_app_page.getback_to_orignal_window(context.original_window)

