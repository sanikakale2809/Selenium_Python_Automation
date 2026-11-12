# URL: https://testautomationpractice.blogspot.com/
# Test case:
# 1.Open the website.
# 2.Find the country dropdown.
# 3.Create an object of the Select class.
# 4.Print all available options.
# 5.Select India using visible text.
# 6.Print the selected option.
# 7.Select another country using value.
# 8.Print the final selected option.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

dropDown=driver.find_element(By.ID,"country")
s=Select(dropDown)

allCountry=s.options
print(len(allCountry))

for eachCountry in allCountry:
    print(eachCountry.text)

s.select_by_visible_text("India")
time.sleep(5)

print("Selected option:",dropDown.get_attribute("value"))

s.select_by_value("usa")
time.sleep(5)

print("Final Selected option:",dropDown.get_attribute("value"))