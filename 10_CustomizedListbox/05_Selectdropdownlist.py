
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.maximize_window()
driver.get(" https://testautomationpractice.blogspot.com/")
time.sleep(10)


SortedList=driver.find_element(By.XPATH,"//select[@id='animals']")

SortedList.click()

for i in range(0,10):
    SortedList.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)

for i in range(0,10):
    SortedList.send_keys(Keys.ARROW_UP)
    time.sleep(2)