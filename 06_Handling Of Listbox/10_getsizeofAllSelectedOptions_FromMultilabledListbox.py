import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

colors=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colors)


s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)


allSelectedOptionsAddress=s.all_selected_options

size=len(allSelectedOptionsAddress)
print(size)

print("---------------------------")

print(len(allSelectedOptionsAddress))

print("---------------------------------")
size2=len(s.all_selected_options)
print(size2)

print("------------------------------")
print(len(s.all_selected_options))