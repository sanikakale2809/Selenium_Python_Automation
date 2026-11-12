# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.	Find elements using a CSS selector that starts with a particular attribute value (^=).
# 2.	Find elements using a CSS selector that contains a value (*=).
# 3.	Find elements using a CSS selector that ends with a value ($=).
# 4.	Print the count of elements found by each selector.
# 5.	Print their text or values.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# 1. CSS selector starts with (^=)
starts = driver.find_elements(By.CSS_SELECTOR, "input[id^='na']")

print("Starts With Count:", len(starts))

for element in starts:
    print("Starts With Value:", element.get_attribute("id"))

# 2. CSS selector contains (*=)
contains = driver.find_elements(By.CSS_SELECTOR, "input[id*='mail']")

print("Contains Count:", len(contains))

for element in contains:
    print("Contains Value:", element.get_attribute("id"))

# 3. CSS selector ends with ($=)
ends = driver.find_elements(By.CSS_SELECTOR, "input[id$='name']")

print("Ends With Count:", len(ends))

for element in ends:
    print("Ends With Value:", element.get_attribute("id"))

time.sleep(3)

# Close browser
driver.quit()
