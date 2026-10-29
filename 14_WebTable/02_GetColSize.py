import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

act=ActionChains(driver)

down=driver.find_element(By.XPATH,"//table[@name='BookTable']")
act.scroll_to_element(down).perform()
time.sleep(5)

AllRows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//td")
print(len(AllRows))


rowSize=len(AllRows)
print(rowSize)


# Get Col Size in a Row

allColAddress=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[4]/td")
print(len(allColAddress))

colSize=len(allColAddress)
print(colSize)