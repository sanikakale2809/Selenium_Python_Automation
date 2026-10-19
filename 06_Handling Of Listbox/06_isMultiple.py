import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


country=driver.find_element(By.XPATH,"//select[@id='country']")
s=Select(country)

result=s.is_multiple
print(result)

if result:
    print("Listbox is of Multi Selectable type")
else:
    print("Listbox is of Single Selectable type")

time.sleep(10)
