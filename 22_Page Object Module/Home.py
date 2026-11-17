from selenium.webdriver.common.by import By


class SwagLabHomePage:

    #1: declare variable/webelements as class variables with private access modifier
    __logoText="//div[@class='app_logo']"


    #2: create constructor of class to initialize driver
    def __init__(self, driver):
        self.driver = driver

    #3: create methods to perform action on webelements

    def getLogoText(self):
        actLogoText=self.driver.find_element(By.XPATH, self.__logoText).text
        return actLogoText
