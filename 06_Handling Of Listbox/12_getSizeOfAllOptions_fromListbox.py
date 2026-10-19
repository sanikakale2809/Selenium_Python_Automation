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

allOptions=s.options

#Apr1
size=len(allOptions)
print(size)

#Apr2
size2=len(allOptions)
print(size2)

#Apr3
print(len(allOptions))

time.sleep(10)