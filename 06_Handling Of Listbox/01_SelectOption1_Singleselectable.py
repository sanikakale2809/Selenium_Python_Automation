import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

#1:identify listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")

#2:Create object of select class
s=Select(country)

#3:Call select class method t select options from list
s.select_by_visible_text("India")    # String text
s.select_by_value("uk")              #value
s.select_by_index(8)                 #int index

time.sleep(10)