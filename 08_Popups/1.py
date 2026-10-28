import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/basic_auth")
# Syntax:   https://username:password@remaingURL
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)



time.sleep(5)
