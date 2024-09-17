from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then ('verify circle page includes {expected} benefits')
def verify_benefits(context, expected):
    benefits=context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components']")
    assert len(benefits)==int(expected), f'{expected} benefit blocks but got {len(benefits)}'
    print(benefits)