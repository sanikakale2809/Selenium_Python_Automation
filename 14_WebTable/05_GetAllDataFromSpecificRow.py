import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

act=ActionChains(driver)
down=driver.find_element(By.XPATH,"//table[@id='taskTable']")
act.scroll_to_element(down).perform()

multiCol=driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr[2]")

for col in multiCol:
    value=col.text
    print(value)