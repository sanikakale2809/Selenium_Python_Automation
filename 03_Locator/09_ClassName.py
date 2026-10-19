import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Bhavesh/Sanika/PycharmProjects/Selenium%20Project/Html%20page/Pratice_page.html")

#Enter LoginButton
driver.find_element(By.CLASS_NAME, "login-button").click()

#Enter register-button
driver.find_element(By.CLASS_NAME, "register-button").click()

#Press search-button
driver.find_element(By.CLASS_NAME, "search-button").click()

time.sleep(5)