import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

act=ActionChains(driver)

down=driver.find_element(By.XPATH,"//a[text()='Download Files']")
act.scroll_to_element(down).perform()
time.sleep(5)


up=driver.find_element(By.XPATH,"//h2[text()='Dynamic Button']")
act.scroll_to_element(up).perform()
time.sleep(5)