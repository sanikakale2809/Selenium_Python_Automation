import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.facebook.com")
time.sleep(5)
driver.quit()




time.sleep(5)