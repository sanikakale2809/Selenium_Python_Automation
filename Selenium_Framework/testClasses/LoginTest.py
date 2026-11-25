import time
from selenium import webdriver

from pageClasses.Login import SwagLabLoginPage

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")

loginObj=SwagLabLoginPage(driver)
loginObj.enterUserName("abc")
time.sleep(2)
loginObj.enterPassword("xyz")
time.sleep(3)
loginObj.clickOnLoginBtn()
time.sleep(3)
actLoginFailedErrorMsg=loginObj.getLoginFailedErrorMsg()
expLoginFailedErrorMsg="Epic sadface: Username and password do not match any user in this service"

if actLoginFailedErrorMsg==expLoginFailedErrorMsg:
    print("Login Failed Test is Passed")
else:
    print("Login Failed Test is Failed")

time.sleep(5)
