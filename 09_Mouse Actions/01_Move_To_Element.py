import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(10)


# Identify Mouse over Element
SignIn=driver.find_element(By.XPATH,"//span[text()='Hello, sign in']")

#Create object of ActionChain Class
act=ActionChains(driver)

#Call method - move to element to display option from mouse over
act.move_to_element(SignIn).perform()

time.sleep(5)
#click on wishlist element
driver.find_element(By.XPATH,"//span[text()='Your Wish List']").click()

time.sleep(5)

