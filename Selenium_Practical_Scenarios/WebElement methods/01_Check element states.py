# URL: https://the-internet.herokuapp.com/checkboxes
# Test case:
# 1.Open the website.
# 2.Find all checkboxes.
# 3.Print the total number of checkboxes.
# 4.Check whether each checkbox is selected.
# 5.Select the unchecked checkbox.
# 6.Print the final selected status of both checkboxes.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

Link=driver.find_element(By.XPATH,"//a[text()='Checkboxes']")
Link.click()

checkBoxes=driver.find_elements(By.XPATH,"//input")
print(len(checkBoxes))

for checkBox in checkBoxes:
    print("Initial Status:",checkBox.is_selected())
    if checkBox.is_selected()==False:
        checkBox.click()

for checkbox in checkBoxes:
    print("Final Status:", checkbox.is_selected())
