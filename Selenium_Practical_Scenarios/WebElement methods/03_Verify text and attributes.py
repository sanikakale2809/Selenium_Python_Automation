# URL: https://the-internet.herokuapp.com/login
# Test case:
# 1.Open the login page.
# 2.Find the username field.
# 3.Print its placeholder or attribute value.
# 4.Find the login button.
# 5.Print its visible text.
# 6.Check whether the button is enabled.
# 7.Enter username and password.
# 8.Click Login.
# 9.Print the resulting message.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)

userName=driver.find_element(By.ID,'username')
userName.send_keys("tomsmith")

print("Username Value:", userName.get_attribute("value"))
# print("Username Placeholder:", userName.get_attribute("placeholder"))

loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")

# Print button text
print("Button Text:", loginButton.text)
print("Login Button is enabled:", loginButton.is_enabled())

password=driver.find_element(By.ID,'password')
password.send_keys("SuperSecretPassword!")
time.sleep(2)
loginButton.click()

mes=driver.find_element(By.ID,"flash")
print("Result Message:", mes.text)

if "You logged into a secure area!" in mes.text:
    print("Test Case Passed")
else:
    print("Test Case Failed")