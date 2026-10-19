import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com")

actTitle=driver.title
print(actTitle)


print("-------------")
print(driver.title)

time.sleep(10)