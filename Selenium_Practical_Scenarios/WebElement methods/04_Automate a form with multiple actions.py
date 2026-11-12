# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Enter name, email and phone.
# 2.Clear and re-enter the email.
# 3.Check whether the address textarea is displayed.
# 4.Enter an address.
# 5.Print the entered values.
# 6.Verify that all fields are enabled.
# 7.Print the final result.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

Name=driver.find_element(By.XPATH,"//input[@id='name']")
Name.send_keys("Sanika kale")

Email=driver.find_element(By.XPATH,"//input[@id='email']")
Email.send_keys("asd@gmail.com")
Email.clear()
Email.send_keys("Sanika@gmail.com")

Phone=driver.find_element(By.XPATH,"//input[@id='phone']")
Phone.send_keys("+91999999999")
time.sleep(5)

Address=driver.find_element(By.XPATH,"//textarea[@id='textarea']")
print("Textarea is displayed:",Address.is_displayed())
Address.send_keys("Amaravati")
time.sleep(5)

print("NameValue:",Name.get_attribute("value"))
print("Email:",Email.get_attribute("value"))
print("Phone:",Phone.get_attribute("value"))
print("AddressValue:",Address.get_attribute("value"))

print("Name field is enabled:",Name.is_enabled())
print("Email field is enabled:",Email.is_enabled())
print("Phone field is enabled:",Phone.is_enabled())
print("Address field is enabled:",Address.is_enabled())

