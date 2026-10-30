import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


# driver.find_element(By.CSS_SELECTOR,"input[placeholder$='Phone']").send_keys("+1 555 555 555 555")
driver.find_element(By.CSS_SELECTOR,"[placeholder$='Phone']").send_keys("1234567898")
time.sleep(2)