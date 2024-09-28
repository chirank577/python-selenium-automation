from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then ('Verify that correct product is shown for {item}')
def search_prod(context, item):
    context.app.search_result.verify_result(item)



