import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

# driver.find_element(By.CSS_SELECTOR,"input#name").send_keys("sanika kale")
# driver.find_element(By.CSS_SELECTOR,"#name").send_keys("sanika kale")
driver.find_element(By.CSS_SELECTOR,"*#name").send_keys("sanika kale")
time.sleep(2)