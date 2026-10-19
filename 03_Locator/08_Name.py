import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Bhavesh/Sanika/PycharmProjects/Selenium%20Project/Html%20page/Pratice_page.html")

driver.maximize_window()
#Enter Firstname
driver.find_element(By.NAME,"firstName").send_keys("Sanikakale")

#Enter Email
driver.find_element(By.NAME,"email").send_keys("s12345@gmail.com")

#Enter city
driver.find_element(By.NAME,"city").send_keys("Amravati")

#Press submit Button
driver.find_element(By.NAME,"submitButton").click()

time.sleep(5)