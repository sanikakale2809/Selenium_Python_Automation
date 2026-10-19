import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Bhavesh/Sanika/PycharmProjects/Selenium%20Project/Html%20page/Pratice_page.html")

#Enter Username
driver.find_element(By.ID,"username").send_keys("Sanikakale")

#Enter Password
driver.find_element(By.ID,"password").send_keys("s@12345")

#Press Login Button
driver.find_element(By.ID,"loginBtn").click()

time.sleep(5)