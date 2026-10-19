import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("xyz")

#Enter Email
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")

#Enter Phone
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8767242785")

#Enter Address
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("Katpur,morshi,Amaravati")
time.sleep(10)