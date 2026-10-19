import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sanika")

attr1=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
print(attr1)

time.sleep(5)