from selenium.webdriver.common.by import By

#POM class
class SwagLabMainPage:

    # 1: declare variable/webelements as class variables
    __MainPage="//button[@id='react-burger-menu-btn']"
    __LogOutBtn="//a[@id='logout_sidebar_link']"

    # 2: create constructor of class to initialize driver
    def __init__(self,driver):
        self.driver=driver

    # 3: create methods to perform action on webelements
    # Click LogOut Button
    def MainPage(self):
        self.driver.find_element(By.XPATH, self.__MainPage).click()

    def LogOut(self):
        self.driver.find_element(By.XPATH, self.__LogOutBtn).click()