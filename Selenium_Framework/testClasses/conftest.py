import pytest
from selenium import webdriver
from utilityClasses.UtilityFile import CommonFunction


# @pytest.fixture
# def setup():
#     driver=webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://www.saucedemo.com/")
#     return driver

#update setup fixture with parameterization
# modify openBrowser fixture
@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(CommonFunction.getAppCred("URL"))
        return driver
    elif browser == "edge":
        driver=webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(CommonFunction.getAppCred("URL"))
        return driver
    elif browser == "firefox":
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(CommonFunction.getAppCred("URL"))
        return driver
    else:
        raise ValueError(f"Unsupported browser: {browser}")


#set default browser
def pytest_addoption(parser):
   parser.addoption("--browser", action="store", default="edge")


#get browser name from cmd line
@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")


#It is hook for adding environment info into Report (customize info in report)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
   metadata['Project Name'] = 'Swag Labs'
   metadata['Module Name'] = 'Login'
   metadata['Tester Name'] = 'Sanika'