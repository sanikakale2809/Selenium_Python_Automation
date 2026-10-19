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

s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)


time.sleep(5)

s.deselect_by_index(0)
s.deselect_by_value("blue")
s.deselect_by_visible_text("Green")

time.sleep(5)