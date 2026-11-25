import time
from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage



class Test_SwagLabLoginPage:

    def test_loginWithValidData (self,setup):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("secret_sauce")
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
            assert False

        time.sleep(2)
        driver.quit()


    def test_loginWithInvalidData (self,setup):
        driver=setup
        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("abc")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        time.sleep(3)
        actLoginFailedMsg=loginObj.getLoginFailedErrorMsg()
        expLoginFailedMsg="Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedMsg == expLoginFailedMsg:
            print("Login Failed Test is Passed")
            assert True
        else:
            print("Login Failed Test is Failed")
            assert False
        time.sleep(3)
        driver.quit()
            


