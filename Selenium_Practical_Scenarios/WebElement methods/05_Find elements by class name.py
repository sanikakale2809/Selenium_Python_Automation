# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Find all elements with a particular class name.
# 2.Print the count.
# 3.Print the text of each element.
# 4.Find a specific element using class name.
# 5.Check whether it is displayed.
# 6.Print its tag name and text.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

# Find all elements using class name
allElement = driver.find_elements(By.CLASS_NAME, "form-group")

# Print total elements
print("Total Elements:", len(allElement))

# Print text of each element
for element in allElement:
    print("Element Text:", element.text)

# Find a specific element using class name
specificElement = driver.find_element(By.CLASS_NAME, "form-group")

# Check whether element is displayed
print("Element Displayed:", specificElement.is_displayed())

# Print tag name
print("Tag Name:", specificElement.tag_name)

# Print element text
print("Element Text:", specificElement.text)

time.sleep(3)
driver.quit()
