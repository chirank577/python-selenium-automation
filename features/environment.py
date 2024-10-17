from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature



def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait= WebDriverWait(context.driver, timeout=15)
    context.app=Application(context.driver)

def before_scenario(context, scenario):
    logger.info(f'Started scenario:  {scenario.name}')
    browser_init(context)


def before_step(context, step):
    logger.info(f'Started step:  {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.info(f'Step failed:  {step}')


def after_scenario(context, feature):
    context.driver.quit()
