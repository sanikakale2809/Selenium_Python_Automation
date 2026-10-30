import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#Enter EMail
# driver.find_element(By.CSS_SELECTOR,"[placeholder*=' EMail']").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[placeholder*=' EMail']").send_keys("abc@gmail.com")
time.sleep(2)