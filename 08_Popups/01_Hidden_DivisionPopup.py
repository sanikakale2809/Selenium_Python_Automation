import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.mobikwik.com/")
time.sleep(2)

#click on login button
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()
time.sleep(2)


#Enter Mobile number
driver.find_element(By.XPATH,"//input[@name='userId']").send_keys("8767242785")
time.sleep(2)


# Click on Get OTP
driver.find_element(By.XPATH,"//button[@class='lfa-cta']").click()
time.sleep(5)