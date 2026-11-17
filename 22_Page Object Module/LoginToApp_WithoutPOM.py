import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")

#Enter UN
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
time.sleep(1)

#Enter PWD
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
time.sleep(1)

#click on login button
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(2)


#get act logo text
actLogoText=driver.find_element(By.XPATH,"//div[@class='app_logo']")
expLogoText="Swag Labs"

if actLogoText==expLogoText:
    print("Login Test is Passed")
else:
    print("Login Test is Failed")

time.sleep(3)
driver.quit()
