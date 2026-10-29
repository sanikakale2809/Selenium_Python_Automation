import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


#Enter Name
# driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("Sanika kale")
# driver.find_element(By.CSS_SELECTOR,"*.form-control").send_keys("Sanika ")
driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("abc")

time.sleep(2)