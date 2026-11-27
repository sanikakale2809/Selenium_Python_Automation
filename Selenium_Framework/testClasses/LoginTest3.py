#Create utility code inside UtilityFile.py
#Call method in test file
# App 1

import time

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction


class TestSwagLabLoginPage:
    def test_LoginWithValidData(self,setup):
        driver = setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("secret_sauce")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        homeObj = SwagLabHomePage(driver)
        actHeaderName = homeObj.getLogoText()
        expHeaderName = "SwagLab"

        if actHeaderName == expHeaderName:
            print("Login Test is Passed")
            assert True
        else:
            print("Login Test is Failed")
            CommonFunction.captureSS(driver,"test_LoginWithValidData")
            assert False

    def test_LoginWithInvalidData(self,setup):
        driver = setup

        login = SwagLabLoginPage(driver)
        login.enterUserName("abc")
        time.sleep(2)
        login.enterPassword("xyz")
        time.sleep(2)
        login.clickOnLoginBtn()
        time.sleep(2)
        actLoginFailedErrorMsg = login.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            print("Login Failed Test is Passed")
            assert True
        else:
            print("Login Failed Test is Failed")
            CommonFunction.captureSS(driver, "test_TC2_loginWithInvalidData")
            assert False

        time.sleep(3)
        driver.quit()