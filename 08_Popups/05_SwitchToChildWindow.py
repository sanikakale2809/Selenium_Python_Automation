import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dri=webdriver.Chrome()
dri.maximize_window()
dri.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#Click on New Window from Main Page
dri.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(5)


#get child Window Id
Id=dri.window_handles                #   [Main Page[0],child Window[2]]


#Switch to Child window
dri.switch_to.window(Id[1])


#click on Training Link from Child Window
dri.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(2)

time.sleep(5)