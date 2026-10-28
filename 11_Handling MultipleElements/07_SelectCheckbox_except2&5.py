# Select all checkboxes except 2nd & 5th (Handling of multiple elements)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

Checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")
print(len(Checkboxes))

id=1
for checkbox in Checkboxes:
    if id!=2 and id!=5:
        checkbox.click()
        time.sleep(1)
    id+=1

time.sleep(5)