import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://testautomationpractice.blogspot.com/")



#click on Simple Alert button
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()

#click on Confirmation Alert
driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()

#click on Prompt Alert
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()

#click on Apple link
driver.find_element(By.XPATH,"//a[text()='Apple']").click()

time.sleep(20)

time.sleep(10)