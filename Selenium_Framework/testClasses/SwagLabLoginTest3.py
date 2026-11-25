import time
from pageClasses.Login import SwagLabLoginPage
from pageClasses.Home import SwagLabHomePage
from utilityClasses.UtilityFile import CommonFunction


class TestSwagLabLoginPage:

    def test_loginWithValidData(self,setup,request):
        driver=setup

        loginObj=SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("secret_sauce")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        homeObj=SwagLabHomePage(driver)
        actLogoText=homeObj.getLogoText()
        expLogoText="Swag Lab"
        if actLogoText == expLogoText:
            print("Login Test Case Passed")

        else:
            print("Login Test Case Failed")
            CommonFunction.captureSS(driver,request.node.name)

    def test_loginWithInvalidData(self, setup,request):
        driver = setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("abc")
        time.sleep(2)
        loginObj.enterPassword("xyz")
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
