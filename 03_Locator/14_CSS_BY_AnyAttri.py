import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

# Enter Name
# driver.find_element(By.CSS_SELECTOR,"input[id='name']").send_keys("Sanika")
# driver.find_element(By.CSS_SELECTOR,"*[id='name']").send_keys("Sanika")
# driver.find_element(By.CSS_SELECTOR,"[id='name']").send_keys("Sanika")
driver.find_element(By.CSS_SELECTOR,"[id='name'][placeholder='Enter Name']").send_keys("Sanika")
time.sleep(2)