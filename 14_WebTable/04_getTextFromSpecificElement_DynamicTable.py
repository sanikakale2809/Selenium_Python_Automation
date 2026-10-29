import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


networkSpeedOfChrome=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Chrome']//parent::tr/td[contains(text(),'Mbps')]").text
print(networkSpeedOfChrome)

cpuValueOfFirefox=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Firefox']//parent::tr/td[contains(text(),'%')]").text
print(cpuValueOfFirefox)

time.sleep(5)