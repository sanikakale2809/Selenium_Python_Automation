import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

colors=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colors)

result=s.is_multiple
print(result)

if result:
    print("Listbox is of Multi Selectable type")
else:
    print("Listbox is of Single Selectable type")