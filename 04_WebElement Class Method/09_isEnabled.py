import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)


result=driver.find_element(By.XPATH,"//input[@id='login-button']").is_enabled()
print(result)


if result:
    print("Element is enabled")
else:
    print("Element is disenabled")


time.sleep(5)
