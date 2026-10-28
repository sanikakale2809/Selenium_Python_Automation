import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


Checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")
print(len(Checkboxes))

# Select checkboxes
for checkbox in Checkboxes:
    checkbox.click()
    time.sleep(2)

time.sleep(5)

# De-select checkboxes
for checkbox in Checkboxes:
    checkbox.click()
    time.sleep(2)

time.sleep(5)
