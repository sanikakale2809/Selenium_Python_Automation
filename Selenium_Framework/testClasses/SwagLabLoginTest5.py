import time
from selenium import webdriver

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction


class Test_SwagLabLogin:

    logger=CommonFunction.loggen()

    def test_TC1_loginWithValidData(self,setup,request):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---clicked on login button---")
        time.sleep(3)

        homeObj = SwagLabHomePage(driver)
        actLogoText = homeObj.getLogoText()
        expLogoText = "Swag Labs"

        if actLogoText == expLogoText:
            self.logger.info("---Login Test is Passed---")
            assert True
        else:
            self.logger.info("---Login Test is Failed---")
            CommonFunction.captureSS(driver,request.node.name)
            assert False

        time.sleep(2)
        driver.quit()

    def test_TC2_loginWithInvalidData(self,setup,request):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---Clicked o login button---")
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()

