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

# s.select_by_index(0)
# s.select_by_index(1)
# s.select_by_index(2)

allOptionsAddress=s.options

for eachOptionsAddress in allOptionsAddress:
    s1=eachOptionsAddress.text
    print(s1)

time.sleep(5)