# URL: https://practicetestautomation.com/practice-test-login/
# Test case:
# 1.Open the login page.
# 2.Enter the username student.
# 3.Enter the password Password123.
# 4.Print the entered username.
# 5.Click the Submit button.
# 6.Verify whether the login is successful.
# 7.Print the success message.
# 8.Close the browser.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

userName=driver.find_element(By.XPATH,"//input[@id='username']")
passWord=driver.find_element(By.XPATH,"//input[@id='password']")
userName.send_keys("student")
passWord.send_keys("Password123")
submitButton=driver.find_element(By.XPATH,"//button[@id='submit']")
submitButton.click()
time.sleep(10)

message=driver.find_element(By.XPATH,"//h1")
print("Success Message:",message)

if message.is_displayed():
    print("Login Successfully")
else:
    print("Login Failed")
    
print("After login url:",driver.current_url)
print("After login Message:",driver.title)

driver.find_element(By.XPATH,"//a[text()='Log out']").click()

time.sleep(5)
# driver.close()