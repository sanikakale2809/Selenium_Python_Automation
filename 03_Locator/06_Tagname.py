import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Bhavesh/Sanika/PycharmProjects/Selenium%20Project/Html%20page/Pratice_page.html")

#Enter UserName
driver.find_element(By.TAG_NAME,"input").send_keys("sanikakale")

time.sleep(10)