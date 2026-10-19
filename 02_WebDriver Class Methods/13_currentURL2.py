import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com")


currentAppUrl=driver.current_url
expAppUrl="https://www.google.com"

if currentAppUrl==expAppUrl:
    print("Navigate to right URL")
else:
    print("Navigate to wrong URL")
