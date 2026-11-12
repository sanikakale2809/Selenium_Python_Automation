# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Locate the name field using #id.
# 2.Locate the email field using input[id='email'].
# 3.Locate the phone field using input#phone.
# 4.Locate a textarea using its tag name.
# 5.Enter values in all fields.
# 6.Print the values.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

name=driver.find_element(By.CSS_SELECTOR,'input#name')
email= driver.find_element(By.CSS_SELECTOR,"input[id='email']")
phone=driver.find_element(By.CSS_SELECTOR,"input#phone")
Address=driver.find_element(By.CSS_SELECTOR,"textarea#textarea")
name.send_keys("Sanika Kale")
email.send_keys("sanika@gmail.com")
phone.send_keys("1234567898")
Address.send_keys("Amaravati")
time.sleep(2)

print("Name Field:",name.get_attribute("value"))
print("Email Field:",email.get_attribute("value"))
print("Phone Field:",phone.get_attribute("value"))
print("Address Field:",Address.get_attribute("value"))