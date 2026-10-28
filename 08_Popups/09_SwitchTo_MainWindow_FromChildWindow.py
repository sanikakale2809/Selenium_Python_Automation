import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#Click on NewTab on Main Page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(5)

#get Child Window IDs
IDs=driver.window_handles                     # [Main Page[0],Child Window [1]]

# Window to child window
driver.switch_to.window(IDs[1])

#click on Training Link from Child Window
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(2)


ID=driver.window_handles
driver.switch_to.window(ID[0])
time.sleep(6)
