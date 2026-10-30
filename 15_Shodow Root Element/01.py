import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://watir.com/examples/shadow_dom.html")
time.sleep(2)


driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("abc")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='shadow_host']").shadow_root.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
time.sleep(2)
