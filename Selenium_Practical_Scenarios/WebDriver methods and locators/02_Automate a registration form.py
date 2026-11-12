# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Open the website and maximize the browser.
# 2.Enter the name, email, phone number and address.
# 3.Clear the name field and enter a different name.
# 4.Print all entered field values.
# 5.Print the page title.
# 6.Close the browser.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

Name=driver.find_element(By.ID,"name")
Email=driver.find_element(By.ID,"email")
Phone=driver.find_element(By.ID,"phone")
Address=driver.find_element(By.ID,"textarea")

Name.send_keys("abc")
Email.send_keys("sanika@gmail.com")
Phone.send_keys("1234567897")
Address.send_keys("Amaravati")
time.sleep(5)

Name.clear()
Name.send_keys("Sanika Kale")

print("Name Field:", Name.get_attribute("value"))
print("Email Field:", Email.get_attribute("value"))
print("Phone Field:", Phone.get_attribute("value"))
print("Address Field:", Address.get_attribute("value"))

print("Page Title:",driver.title)
driver.quit()
