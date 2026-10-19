import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")


sunday=driver.find_element(By.XPATH,"//input[@id='sunday']")

result=sunday.is_selected()
if result:
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")
time.sleep(2)


print("Selecting the checkbox")
sunday.click()
time.sleep(2)

result2=sunday.is_selected()
if result2:
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")


time.sleep(5)
