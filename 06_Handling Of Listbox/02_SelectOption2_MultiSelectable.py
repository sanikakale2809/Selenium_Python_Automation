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

s.select_by_value("red")              #string value
s.select_by_visible_text("Blue")      #string text
s.select_by_index(3)                  #index

time.sleep(5)