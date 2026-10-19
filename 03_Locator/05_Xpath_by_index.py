import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"//input[@class='form-control']").send_keys("abc")


#Enter Email
driver.find_element(By.XPATH,"(//input[@class='form-control'])[2]").send_keys("xyz")


#Enter phone
driver.find_element(By.XPATH,"(//input[@class='form-control'])[3]").send_keys("1234567890")

time.sleep(10)