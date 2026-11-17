import time
from selenium import webdriver
from Login import SwagLabLoginPage
from Home import SwagLabHomePage


driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")

loginObj=SwagLabLoginPage(driver)
loginObj.enterUserName("standard_user")
time.sleep(2)
loginObj.enterPassword("secret_sauce")
time.sleep(3)
loginObj.clickOnLoginBtn()
time.sleep(3)

homeObj=SwagLabHomePage(driver)
actLogoText=homeObj.getLogoText()
expLogoText="Swag Labs"

if actLogoText==expLogoText:
    print("Login Test is Passed")
else:
    print("Login Test is Failed")


time.sleep(5)