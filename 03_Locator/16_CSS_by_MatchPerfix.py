import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


driver.find_element(By.CSS_SELECTOR,"button[class^='st']").click()

driver.find_element(By.CSS_SELECTOR,"[class^='st']").click()
time.sleep(2)