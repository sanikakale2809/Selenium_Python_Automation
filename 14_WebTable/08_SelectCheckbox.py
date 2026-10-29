# In Pagination WebTable  -> select checkbox of name table
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

act=ActionChains(driver)
down=driver.find_element(By.XPATH,"//table[@id='productTable']")
act.scroll_to_element(down).perform()
time.sleep(5)

# Locate the cell containing the product name Laptop,
# move to its parent row, and locate the checkbox in that row
driver.find_element(By.XPATH,"//table[@id='productTable']//td[text()='Laptop']/parent::tr//input[@type='checkbox']").click()
time.sleep(2)

# Close the browser and end the WebDriver session
driver.quit()