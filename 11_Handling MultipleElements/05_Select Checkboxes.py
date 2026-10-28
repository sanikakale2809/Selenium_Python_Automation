# Select all checkboxes in forward direction & deselect in reverse order
# Ref url- https://testautomationpractice.blogspot.com/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

# Find checkboxes of Days
Checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")

# Select all checkboxes forward
for checkbox in Checkboxes:
    checkbox.click()
    time.sleep(1)


# De-Select all checkboxes in reverse
for checkbox in reversed(Checkboxes):
    checkbox.click()
    time.sleep(1)
driver.quit()