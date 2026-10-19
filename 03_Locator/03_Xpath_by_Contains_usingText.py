import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)


#click on link - Hidden Elements & AJAX
driver.find_element(By.XPATH,"//a[contains(text(),'AJAX')]").click()

#click on Errorcode 500
driver.find_element(By.XPATH,"//a[contains(text(),'500')]").click()


time.sleep(10)