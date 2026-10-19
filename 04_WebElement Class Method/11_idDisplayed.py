import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

try:
    result=driver.find_element(By.XPATH,"//input[@id='SUNDAY']").is_displayed()
except NoSuchElementException:
    result=False
    print("Exeption handled: Element not found")
print(result)

if result:
    print("Element is displayed")
else:
    print("Element is not displayed")

time.sleep(5)

