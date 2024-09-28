from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then ('Verify Sign In form opened')
def Sig_in_opened(context):
    context.app.Signin_page.SIGN_IN_VERIFICATION()

@when('click on email{email} and enter email address')
def Enter_email(context, email):
    context.app.Signin_page.Enter_email(email)

@when ('click on password {Password}  enter valid password')
def Enter_Password(context, Password):
    context.app.Signin_page.Enter_password(Password)
@when('click on sign in with password')
def Click_on_signin_with_pswd_btn(context):
    context.app.Signin_page.Click_on_signin_with_pswd_btn()


    sleep(3)
@then ('Verify user can sign in using valid email address and password')
def Verify_log_in_successful(context):
    context.app.header.VERIFY_USER_CAN_SIGN_IN_WITH_VALID_ID()