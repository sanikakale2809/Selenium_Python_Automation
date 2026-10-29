import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(5)

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("samsung")
time.sleep(2)


allOptions=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]//li")

expText="samsung s26 ultra"


for eachOption in allOptions:
    actText=eachOption.text
    if actText==expText:
        eachOption.click()
        break
time.sleep(5)