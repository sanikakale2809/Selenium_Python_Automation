import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

attr1=driver.find_element(By.XPATH,"//input[@id='singleFileInput']").get_attribute("type")
print(attr1)


attr2=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("placeholder")
print(attr2)

time.sleep(5)