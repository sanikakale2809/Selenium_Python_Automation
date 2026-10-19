import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://facebook.com")
time.sleep(2)
driver.minimize_window()




time.sleep(10)