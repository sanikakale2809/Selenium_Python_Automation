import time
from selenium import webdriver
from Login import SwagLabLoginPage
from MainPage import SwagLabMainPage
from Home import SwagLabHomePage


driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")

loginObj = SwagLabLoginPage(driver)
loginObj.enterUserName("standard_user")
time.sleep(2)
loginObj.enterPassword("secret_sauce")
time.sleep(2)
loginObj.clickOnLoginBtn()
time.sleep(2)

HomeObj = SwagLabHomePage(driver)
actLogoText=HomeObj. getLogoText()
expLogoText="Swag Labs"

if actLogoText==expLogoText:
    print("Login Successful")
else:
    print("Login Failed")


MainObj = SwagLabMainPage(driver)
MainObj.MainPage()
time.sleep(2)
MainObj.LogOut()
time.sleep(2)

actlogintext=loginObj.getLogoText()
exploginText="Swag Labs"

if actlogintext==exploginText:
    print("Logout Successful")
else:
    print("Logout Failed")