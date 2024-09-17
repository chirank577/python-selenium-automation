from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then ('Verify that correct product is shown for {item}')
def search_prod(context, item):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert item in actual_result, f' Expected {item} actual result {actual_result}'
    sleep(2)


