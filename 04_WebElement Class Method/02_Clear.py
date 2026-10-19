import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# 1st app
#Enter Name
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sanika")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sanika kale")


# 2ed app
#Enter Email
Email=driver.find_element(By.XPATH,"//input[@id='email']")
Email.send_keys("abc123@gmail.com")
time.sleep(2)
Email.clear()
time.sleep(2)
Email.send_keys("Sanika123@gmail.com")


time.sleep(2)