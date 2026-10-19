import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

start=driver.find_element(By.XPATH,"//button[text()='START']")
start.screenshot( r"C:\Users\Bhavesh\Sanika\PycharmProjects\Selenium Project\Screenshot\start_button.png")
