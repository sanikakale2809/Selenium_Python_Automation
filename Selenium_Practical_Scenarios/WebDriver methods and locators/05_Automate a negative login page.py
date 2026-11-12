# Test case 2: Negative username test
# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

userName=driver.find_element(By.XPATH,"//input[@id='username']")
passWord=driver.find_element(By.XPATH,"//input[@id='password']")
userName.send_keys("students")
passWord.send_keys("Password123")
submitButton=driver.find_element(By.XPATH,"//button[@id='submit']")
submitButton.click()

message1=driver.find_element(By.XPATH,"//div[@id='error']")
print("Error Message:",message1.text)

if message1.is_displayed():
    print("Message displayed")
else:
    print("Message not displayed")

time.sleep(10)

#
# Test case 3: Negative password test
# Open page
# Type username student into Username field
# Type password incorrectPassword into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your password is invalid!


userName=driver.find_element(By.XPATH,"//input[@id='username']")
passWord=driver.find_element(By.XPATH,"//input[@id='password']")
userName.send_keys("student")
passWord.send_keys("Password12")
submitButton=driver.find_element(By.XPATH,"//button[@id='submit']")
submitButton.click()

message2=driver.find_element(By.XPATH,"//div[@id='error']")
print("Error Message:",message2.text)

if message2.is_displayed():
    print("Message displayed")
else:
    print("Message not displayed")