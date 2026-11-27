# Writing 1st TestCase  using POM(Page Object Module) design pattern
import time
from selenium import webdriver
from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage

class TestSwagLabLoginTest:


    def test_LoginWithValideData(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")


        loginObj=SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("secret_sauce")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)


        homeObj = SwagLabHomePage(driver)
        actHeaderName=homeObj.getLogoText()
        extHeaderName="Swag Labs"

        if actHeaderName==extHeaderName:
            assert True
        else:
            assert False

        time.sleep(3)
        driver.close()

    def test_LoginWithoutValideData(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")

        login = SwagLabLoginPage(driver)
        login.enterUserName("abc")
        time.sleep(2)
        login.enterPassword("xyz")
        time.sleep(2)
        login.clickOnLoginBtn()
        time.sleep(2)
        actErrorMsg=login.getLoginFailedErrorMsg()
        extErrorMsg=("Epic sadface: Username and password do not match any user in this service")
        print("actErrorMsg=",actErrorMsg)
        print("extErrorMsg=",extErrorMsg)

        if actErrorMsg==extErrorMsg:
            assert True
        else:
            assert False

        time.sleep(5)