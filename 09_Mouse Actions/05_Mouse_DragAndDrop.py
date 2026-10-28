import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/drag_drop.html")
time.sleep(5)

drg=driver.find_element(By.XPATH,"(//li[@class='block13 ui-draggable'])[1]")
drp=driver.find_element(By.XPATH,"(//div[@class='ui-widget-content'])[3]")

act=ActionChains(driver)

act.drag_and_drop(drg,drp).perform()
time.sleep(5)