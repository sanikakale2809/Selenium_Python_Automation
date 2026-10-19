import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

colors = driver.find_element(By.XPATH, "//select[@id='colors']")

s = Select(colors)

# Apr1
s1 = s.first_selected_option
firstSelectedOption = s1.text
print(firstSelectedOption)

# Apr2
firstSelectOptionValue2 = s.first_selected_option.text
print(firstSelectOptionValue2)

# Apr3
print(s.first_selected_option.text)

time.sleep(5)

