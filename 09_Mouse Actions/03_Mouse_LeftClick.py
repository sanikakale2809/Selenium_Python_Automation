import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)

# Identify Mouse over Element
menu=driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']")

#Create object of ActionChain Class
act=ActionChains(driver)


# Apr 1
# Call method - move to element to display option from mouse over
# act.move_to_element(menu).perform()
# act.click().perform()

# Apr 2
# act.move_to_element(menu).context_click().perform()

# Apr 3
act.click(menu).perform()

time.sleep(5)