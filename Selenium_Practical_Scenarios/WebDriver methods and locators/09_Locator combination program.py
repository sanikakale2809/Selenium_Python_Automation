# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Locate the name field using ID.
# 2.Locate the email field using CSS selector.
# 3.Locate the phone field using XPath.
# 4.Locate the address field using a suitable locator.
# 5.Enter different values in all fields.
# 6.Print all values using get_attribute("value").
# 7.Clear the phone field and enter a new number.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

Name=driver.find_element(By.ID,"name")
Name.send_keys("Sanika kale")
Email=driver.find_element(By.CSS_SELECTOR,"*#email")
Email.send_keys("sanika@gmail.com")
Phone=driver.find_element(By.XPATH,"//input[@id='phone']")
Phone.send_keys("123-456-7890")
Address=driver.find_element(By.XPATH,"//textarea[@id='textarea']")
Address.send_keys("Amaravati")

print("Name Field:",Name.get_attribute("value"))
print("Email Field:",Email.get_attribute("value"))
print("Phone Field:",Phone.get_attribute("value"))
print("Address Field:",Address.get_attribute("value"))
time.sleep(5)
Phone.clear()
Phone.send_keys("2345678234")
time.sleep(5)
print("Phone Field:",Phone.get_attribute("value"))
