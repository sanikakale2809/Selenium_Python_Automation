import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://facebook.com")
time.sleep(2)
driver.get("https://google.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)




time.sleep(10)
