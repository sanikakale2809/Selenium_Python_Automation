import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)


driver.save_screenshot( r"C:\Users\Bhavesh\Sanika\PycharmProjects\Selenium Project\Screenshot\FullPageScreenshot.png")