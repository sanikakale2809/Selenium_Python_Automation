import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)              #syntax of implicit wait


driver.find_element(By.XPATH,"//label[text()='Name:']//following-sibling::input[2]").send_keys("abc")

time.sleep(5)