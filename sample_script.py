from pyexpat.errors import messages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.implicitly_wait(4)
wait= WebDriverWait(driver,timeout=20)

# open the url
# driver.get('https://www.google.com/')
#
# # populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Car')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()

# verify search results
# assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()


#search for energy drink

# open the url
driver.get('https://www.target.com/')
#search field=> enter water


driver.find_element(By.XPATH,"//input[@data-test='@web/Search/SearchInput']").send_keys('energy drink')

wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test='@web/Search/SearchButton']"))).click()
# driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
# sleep(6)

#verification
actual_result= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-test='resultsHeading']"))).text
expected_result='energy drink'
assert expected_result in actual_result, f' Expected {expected_result} actual result {actual_result}'
print('Test case Passed')


