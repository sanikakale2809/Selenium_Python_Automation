import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

allLinks=driver.find_elements(By.XPATH,"//a")      #[webElement1, webelement2, webelement3....]
print("Total Links in a webpage: ",len(allLinks))

for eachLink in allLinks:
    s1=eachLink.text
    print(s1)


time.sleep(5)

