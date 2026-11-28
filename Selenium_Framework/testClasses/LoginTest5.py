# Call config.ini file in values in Test class

import time

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction

class TestSwagLabLoginPage:
    def test_LoginWithValidData(self,setup,request):
        driver = setup

        loginObj=SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        homeObj = SwagLabHomePage(driver)
        actHeaderName = homeObj.getLogoText()
        expHeaderName = "Swag Labs"

        if actHeaderName == expHeaderName:
            print("Login Test is Passed")
            assert True
        else:
            print("Login Test is Failed")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        driver.quit()

    def test_LoginWithInvalidData(self, setup, request):
        driver = setup

        login = SwagLabLoginPage(driver)
        login.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        time.sleep(2)
        login.enterPassword(CommonFunction.getAppCred("invalidPassword"))
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
            CommonFunction.captureSS(driver, request.node.name)
            assert False


        driver.quit()