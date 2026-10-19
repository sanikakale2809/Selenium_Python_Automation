import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
text=driver.find_element(By.XPATH,"//button[@id='alertBtn']").text
print(text)


table=driver.find_element(By.XPATH,"//h2[text()='Static Web Table']").text
print(table)
time.sleep(2)