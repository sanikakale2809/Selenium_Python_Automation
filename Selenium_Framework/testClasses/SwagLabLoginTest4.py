import time
from selenium import webdriver

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction


class Test_SwagLabLogin:

    def test_TC1_loginWithValidData(self,setup,request):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        time.sleep(3)

        homeObj = SwagLabHomePage(driver)
        actLogoText = homeObj.getLogoText()
        expLogoText = "Swag Labs"

        if actLogoText == expLogoText:
            print("Login Test is Passed")
            assert True
        else:
            print("Login Test is Failed")
            CommonFunction.captureSS(driver,request.node.name)
            assert False

        time.sleep(2)
        driver.quit()

    def test_TC2_loginWithInvalidData(self,setup,request):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            print("Login Failed Test is Passed")
            assert True
        else:
            print("Login Failed Test is Failed")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()

