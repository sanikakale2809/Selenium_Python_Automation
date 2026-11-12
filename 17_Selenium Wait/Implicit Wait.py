from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(10)