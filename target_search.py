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
driver.get('https://www.target.com/')
#search field=> enter water

driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
sleep(2)

actual_result=driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
sleep(6)
assert driver.find_element(By.ID,'login'), f'sign in element is not found'
sleep(2)

quit()