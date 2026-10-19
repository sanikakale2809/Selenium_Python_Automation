import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Bhavesh/Sanika/PycharmProjects/Selenium%20Project/Html%20page/Pratice_page.html")
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Official").click()

driver.find_element(By.LINK_TEXT, "Repository").click()
time.sleep(5)