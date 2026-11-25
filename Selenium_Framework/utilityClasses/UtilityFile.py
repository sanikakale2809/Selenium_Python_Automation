import logging
from datetime import datetime
import configparser

class CommonFunction:

    # Author Name: Sanika
    # This method is used to capture the screenshot of the current page and save it in the Screenshots folder with the test name and current date & time.
    @staticmethod
    def captureSS(driver,test_name):
        # Current date & time
        current_time=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #Screenshot file name
        screenshot_path = f".\\Screenshots\\{test_name}_{current_time}.png"

        driver.save_screenshot(screenshot_path)
        print("Screenshot captured successfully")


    @staticmethod
    def getAppCred(key):
        config = configparser.RawConfigParser()              # create object of RawConfigParser class
        config.read(".\\Selenium_Framework\\ConfigurationFiles\\config.ini")        #
        value = config.get("App_Credentials", key)
        return value


    @staticmethod
    def getAppURL():
        config = configparser.RawConfigParser()
        config.read(".\\Selenium_Framework\\ConfigurationFiles\\config.ini")        #
        value = config.get("App_Credentials", "URL")
        return value

    @staticmethod
    def getAppUN():
        config = configparser.RawConfigParser()
        config.read(".\\Selenium_Framework\\ConfigurationFiles\\config.ini")  #
        value = config.get("App_Credentials", "username")
        return value

    @staticmethod
    def getAppPWD():
        config = configparser.RawConfigParser()
        config.read(".\\Selenium_Framework\\ConfigurationFiles\\config.ini")  #
        value = config.get("App_Credentials", "password")
        return value

    @staticmethod
    def loggen():
        # Generate filename with current date & time -> convert to string
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f".\\Selenium_Framework\\Logs\\SwagLabLogs_{current_time}.log"

        # The f stands for formatted string literal (also called an f-string)

        logging.basicConfig(filename=log_filename,
                format='%(asctime)s: %(levelname)s: %(message)s',
                datefmt="%Y-%m-%d %H:%M:%S",
                force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


