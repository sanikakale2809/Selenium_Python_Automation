import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Name')]").send_keys("abc")


#Enter EMail
driver.find_element(By.XPATH,"//input[contains(@placeholder,'EMail')]").send_keys("abc@gmail.com")

#Enter Address
driver.find_element(By.XPATH,"//textarea[contains(@id,'area')]").send_keys("xyz")



time.sleep(10)