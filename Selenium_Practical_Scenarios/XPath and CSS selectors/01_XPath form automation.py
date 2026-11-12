# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Find the name field using XPath with ID.
# 2.Find the email field using XPath with an attribute.
# 3.Find the phone field using XPath with a placeholder.
# 4.Enter values in all three fields.
# 5.Print the entered values.
# 6.Clear the email field and enter a new email.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)

Name=driver.find_element(By.XPATH,"//input[@id='name']")

# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1. Find the name field using XPath with ID.
# 2. Find the email field using XPath with an attribute.
# 3. Find the phone field using XPath with a placeholder.
# 4. Enter values in all three fields.
# 5. Print the entered values.
# 6. Clear the email field and enter a new email.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# Find name field using XPath with ID
Name = driver.find_element(By.XPATH, "//input[@id='name']")

# Find email field using XPath with attribute
Email = driver.find_element(By.XPATH, "//input[@type='text']")

# Find phone field using XPath with placeholder
Phone = driver.find_element(By.XPATH, "//input[@placeholder='Enter Phone']")

# Enter values
Name.send_keys("Sanika Kale")
Email.send_keys("sanika@gmail.com")
Phone.send_keys("9999999999")

# Print entered values
print("Name:", Name.get_attribute("value"))
print("Email:", Email.get_attribute("value"))
print("Phone:", Phone.get_attribute("value"))

# Clear email field
Email.clear()

# Enter new email
Email.send_keys("sanika123@gmail.com")

# Print updated email
print("Updated Email:", Email.get_attribute("value"))

time.sleep(3)

# Close browser
driver.quit()
