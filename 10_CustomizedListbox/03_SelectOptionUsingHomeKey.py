import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

#step1: Identify the listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")


#step2: Open listbox option using click method
country.click()

#Navigate To 1st option Home key
country.send_keys(Keys.HOME)


time.sleep(10)