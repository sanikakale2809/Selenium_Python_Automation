import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.facebook.com")

actTitle=driver.title
expTitle="Facebook"

if actTitle==expTitle:
    print("Navigate to proper page")
else:
    print("Navigate to wrong page")


time.sleep(2)