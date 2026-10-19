import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)


#Switch to Frame
driver.switch_to.frame("iframeResult")                                                   #String id/name of the frame

#Click button to display Date and time
driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time')]").click()


#Switch back main page
# driver.switch_to.parent_frame()
driver.switch_to.default_content()

#click on Open menu button from main page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()
time.sleep(10)