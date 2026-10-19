import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


country=driver.find_element(By.XPATH,"//select[@id='country']")
s=Select(country)

#Apr1
s1=s.first_selected_option
selectOptionValue=s1.text
print(selectOptionValue)

# Apr2
selectOptionValue2=s.first_selected_option.text
print(selectOptionValue2)

# Apr3:
print(s.first_selected_option.text)

time.sleep(10)