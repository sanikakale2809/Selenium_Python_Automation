import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


checkboxes=driver.find_elements(By.XPATH,"(//div[@class='form-group'])//input[@type='checkbox']")
print(len(checkboxes))

# Checkboxes=driver.find_elements(By.XPATH,"(//div[@class='form-group'])[4]//input[@type='checkbox']")
# print(len(Checkboxes))

# allCheckboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")
# print(len(allCheckboxes))

#select all checkboxes
for eachCheckbox in checkboxes:
    eachCheckbox.click()
    time.sleep(1)


time.sleep(5)
