import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


# StartStopEle=driver.find_element(By.XPATH,"//button[@class='start' or @class='stop']")
# StartStopEle=driver.find_element(By.XPATH,"//button[text()='START' or text()='STOP']")
# StartStopEle=driver.find_element(By.XPATH,"//button[starts-with(@name,'st')]")
StartStopEle=driver.find_element(By.XPATH,"//button[starts-with(text(),'ST')]")


#click on Start
StartStopEle.click()
time.sleep(3)

#click on STOP
StartStopEle.click()
time.sleep(3)

#click on Start
StartStopEle.click()
time.sleep(3)