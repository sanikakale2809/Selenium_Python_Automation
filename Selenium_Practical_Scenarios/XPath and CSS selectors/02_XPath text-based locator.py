# URL: https://the-internet.herokuapp.com/
# Test case:
# 1.Find the Form Authentication link using text-based XPath.
# 2.Click the link.
# 3.Find the Login button using text-based XPath.
# 4.Print its text.
# 5.Check whether it is displayed and enabled.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(5)

authenticationLink=driver.find_element(By.XPATH,"//a[text()='Form Authentication']")
authenticationLink.click()
time.sleep(5)


loginButton=driver.find_element(By.XPATH,"//button[@class='radius']")
print("Login Button Text:",loginButton.text)
print("Login Button is displayed:",loginButton.is_displayed())
print("Login Button is enabled:",loginButton.is_enabled())