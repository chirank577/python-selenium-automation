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