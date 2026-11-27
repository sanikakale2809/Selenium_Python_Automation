# call logger method in Test class

import time

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction

class TestSwagLabLoginPage:
    logger=CommonFunction.loggen()
    def test_LoginWithValidData(self,setup,request):
        driver = setup

        loginObj=SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        self.logger.info("-----UN Entered-----")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        self.logger.info("-----PWD Entered-----")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        self.logger.info("-----Click on Login Button-----")
        time.sleep(2)

        homeObj = SwagLabHomePage(driver)
        actHeaderName = homeObj.getLogoText()
        expHeaderName = "Swag Labs"

        if actHeaderName == expHeaderName:
            self.logger.info("------Login Test is Passed-----")
            assert True
        else:
            self.logger.info("------Login Test is Failed-----")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

    def test_LoginWithInvalidData(self, setup, request):
        driver = setup

        login = SwagLabLoginPage(driver)
        login.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("-----Username Entered-----")
        time.sleep(2)
        login.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("-----Password Entered-----")
        time.sleep(2)
        login.clickOnLoginBtn()
        self.logger.info("-----Click on Login Btn-----")
        time.sleep(2)
        actLoginFailedErrorMsg = login.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Failed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()