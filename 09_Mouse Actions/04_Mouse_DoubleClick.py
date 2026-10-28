import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(5)

Double=driver.find_element(By.XPATH,"//button[contains(text(),'Double')]")

act=ActionChains(driver)

# Apr1
# act.move_to_element(Double).perform()
# act.double_click().perform()

#Apr 2
# act.move_to_element(Double).double_click().perform()

#Apr 3
act.double_click(Double).perform()
time.sleep(5)