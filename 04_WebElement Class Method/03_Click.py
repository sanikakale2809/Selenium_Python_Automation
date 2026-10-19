import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")


#click on male radio button
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(3)

#click on sunday checkbox
driver.find_element(By.XPATH,"//input[@id='sunday']").click()
time.sleep(3)

#click ErrorCode 400 link
driver.find_element(By.XPATH,"//a[text()='Errorcode 400']").click()


time.sleep(5)
