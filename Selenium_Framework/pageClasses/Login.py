from selenium.webdriver.common.by import By

#POM class
class SwagLabLoginPage:

    #1: declare variable/webelements as class variables
    __UN="//input[@id='user-name']"
    __PWD="//input[@id='password']"
    __LoginBtn="//input[@id='login-button']"
    __loginFailedErrorMsg="//h3[@data-test='error']"

    #2: create constructor of class to initialize driver
    def __init__(self,driver):
        self.driver=driver


    #3: create methods to perform action on webelements

    #Enter UN
    def enterUserName(self,UNValue):
        self.driver.find_element(By.XPATH,self.__UN).send_keys(UNValue)

    #enter password
    def enterPassword(self,pwdValue):
        self.driver.find_element(By.XPATH,self.__PWD).send_keys(pwdValue)

    #click on login button
    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH,self.__LoginBtn).click()

    def getLoginFailedErrorMsg(self):
        actLoginFailedMsg=self.driver.find_element(By.XPATH,self.__loginFailedErrorMsg).text
        return actLoginFailedMsg



